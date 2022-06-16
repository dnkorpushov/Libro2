import os
import shutil
import ebookmeta
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QObject, QThread, pyqtSignal, Qt
from .processdialog_ui import Ui_ProcessDialog
import database


class Worker(QObject):
    currentProcess = pyqtSignal(int, int)
    finished = pyqtSignal()

    def __init__(self, book_info_list, filename_format, author_format, delete_src, backup_src, overwtite_exsits, parent=None):
        super(Worker, self).__init__(parent)
        self.book_info_list = book_info_list
        self.filename_format = filename_format
        self.author_format = author_format
        self.delete_src = delete_src
        self.backup_src = backup_src
        self.overwtite_exists = overwtite_exsits
        self.isRunning = True
        self.errors = []

    def moveFiles(self):
        src = None
        dst = None
        i = 0
        count = len(self.book_info_list)
        for book in self.book_info_list:
            if self.isRunning:
                i += 1
                try:
                    src = book.file
                    meta = ebookmeta.get_metadata(src)
                    new_filename = meta.get_filename_by_pattern(self.filename_format, self.author_format)
                    dst = os.path.normpath(os.path.join(os.path.dirname(meta.file), new_filename))
                    if self.delete_src and self.backup_src:
                        backup = os.path.normpath(src + '.bak')
                        shutil.copy2(src, backup)

                    if not os.path.exists(dst) or self.overwtite_exists:
                        if not os.path.exists(os.path.dirname(dst)):
                            os.makedirs(os.path.dirname(dst))
                        if self.delete_src:
                            shutil.move(src, dst)
                        else:
                            shutil.copy2(src, dst)
                        database.update_filename(book.id, dst)
                    else:
                        raise Exception('Destination file already exsist.')
                    
                    self.currentProcess.emit(i, count)
                except Exception as e:
                    self.currentProcess.emit(i, count)
                    self.errors.append({ 'src': src, 'dest': dst, 'error': str(e) })
            else:
                self.errors.append({'src': None, 'dest': None, 'error': 'User interrupt'})   
                break
        self.finished.emit()

    def kill(self):
        self.isRunning = False


class MoveFilesDialog(QDialog, Ui_ProcessDialog):
    def __init__(self, parent, book_info_list, filename_format, author_format, delete_src, backup_src, overwrite_exists):
        super(MoveFilesDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Rename {0} files'.format(len(book_info_list)))
        if delete_src:
            self.operationName = 'Move'
        else:
            self.operationName = 'Copy'

        self.setWindowFlags(Qt.Dialog | Qt.CustomizeWindowHint | Qt.WindowTitleHint)

        self.progressBar.setMaximum(len(book_info_list))
        self.progressBar.setMinimum(0)
        self.progressLabel.setText('')

        self.thread = QThread()
        self.worker = Worker(book_info_list, filename_format, author_format, delete_src, backup_src, overwrite_exists)
        self.worker.currentProcess.connect(self.setCurrentProcess)
        self.worker.moveToThread(self.thread)
        self.worker.finished.connect(self.thread.quit)

        self.thread.started.connect(self.worker.moveFiles)
        self.thread.finished.connect(self.close)


    def setCurrentProcess(self, index, count):
        self.progressLabel.setText('{0} files... {1} of {2}'.format(self.operationName, index, count))
        self.progressBar.setValue(index)


    def cancelProcess(self):    
        self.worker.kill()


    def getMetadata(self):
        return self.worker.metadata


    def showEvent(self, event):
        self.thread.start()
        
    def getErrors(self):
        return self.worker.errors