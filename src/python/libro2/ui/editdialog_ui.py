# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src\designer\editdialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EditDialog(object):
    def setupUi(self, EditDialog):
        EditDialog.setObjectName("EditDialog")
        EditDialog.resize(862, 474)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(EditDialog)
        self.verticalLayout_2.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cover = QtWidgets.QLabel(EditDialog)
        self.cover.setMinimumSize(QtCore.QSize(169, 260))
        self.cover.setMaximumSize(QtCore.QSize(169, 260))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.cover.setFont(font)
        self.cover.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cover.setFrameShadow(QtWidgets.QFrame.Plain)
        self.cover.setAlignment(QtCore.Qt.AlignCenter)
        self.cover.setWordWrap(True)
        self.cover.setObjectName("cover")
        self.verticalLayout.addWidget(self.cover)
        self.btnLoadFromFile = QtWidgets.QPushButton(EditDialog)
        self.btnLoadFromFile.setObjectName("btnLoadFromFile")
        self.verticalLayout.addWidget(self.btnLoadFromFile)
        self.btnSaveToFile = QtWidgets.QPushButton(EditDialog)
        self.btnSaveToFile.setObjectName("btnSaveToFile")
        self.verticalLayout.addWidget(self.btnSaveToFile)
        spacerItem = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.tabWidget = QtWidgets.QTabWidget(EditDialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.formLayout = QtWidgets.QFormLayout(self.tab)
        self.formLayout.setObjectName("formLayout")
        self.checkTitle = QtWidgets.QCheckBox(self.tab)
        self.checkTitle.setObjectName("checkTitle")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.checkTitle)
        self.textTitle = QtWidgets.QLineEdit(self.tab)
        self.textTitle.setObjectName("textTitle")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.textTitle)
        self.checkAuthor = QtWidgets.QCheckBox(self.tab)
        self.checkAuthor.setObjectName("checkAuthor")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.checkAuthor)
        self.textAuthor = QtWidgets.QLineEdit(self.tab)
        self.textAuthor.setObjectName("textAuthor")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textAuthor)
        self.checkSeries = QtWidgets.QCheckBox(self.tab)
        self.checkSeries.setObjectName("checkSeries")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.checkSeries)
        self.textSeries = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textSeries.sizePolicy().hasHeightForWidth())
        self.textSeries.setSizePolicy(sizePolicy)
        self.textSeries.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.textSeries.setObjectName("textSeries")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.textSeries)
        self.checkSeriesIndex = QtWidgets.QCheckBox(self.tab)
        self.checkSeriesIndex.setObjectName("checkSeriesIndex")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.checkSeriesIndex)
        self.textSeriesIndex = QtWidgets.QLineEdit(self.tab)
        self.textSeriesIndex.setMaximumSize(QtCore.QSize(50, 16777215))
        self.textSeriesIndex.setObjectName("textSeriesIndex")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.textSeriesIndex)
        self.checkTags = QtWidgets.QCheckBox(self.tab)
        self.checkTags.setObjectName("checkTags")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.checkTags)
        self.textTags = ButtonLineEdit(self.tab)
        self.textTags.setObjectName("textTags")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.textTags)
        self.checkLang = QtWidgets.QCheckBox(self.tab)
        self.checkLang.setObjectName("checkLang")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.checkLang)
        self.textLang = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textLang.sizePolicy().hasHeightForWidth())
        self.textLang.setSizePolicy(sizePolicy)
        self.textLang.setMaximumSize(QtCore.QSize(50, 16777215))
        self.textLang.setObjectName("textLang")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.textLang)
        self.checkTranslator = QtWidgets.QCheckBox(self.tab)
        self.checkTranslator.setObjectName("checkTranslator")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.checkTranslator)
        self.textTranslator = QtWidgets.QLineEdit(self.tab)
        self.textTranslator.setObjectName("textTranslator")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.textTranslator)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(7, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkPublishTitle = QtWidgets.QCheckBox(self.tab_2)
        self.checkPublishTitle.setObjectName("checkPublishTitle")
        self.gridLayout_2.addWidget(self.checkPublishTitle, 0, 0, 1, 1)
        self.textPublishTitle = QtWidgets.QLineEdit(self.tab_2)
        self.textPublishTitle.setObjectName("textPublishTitle")
        self.gridLayout_2.addWidget(self.textPublishTitle, 0, 1, 1, 1)
        self.checkPublishPublisher = QtWidgets.QCheckBox(self.tab_2)
        self.checkPublishPublisher.setObjectName("checkPublishPublisher")
        self.gridLayout_2.addWidget(self.checkPublishPublisher, 1, 0, 1, 1)
        self.textPublishPublisher = QtWidgets.QLineEdit(self.tab_2)
        self.textPublishPublisher.setObjectName("textPublishPublisher")
        self.gridLayout_2.addWidget(self.textPublishPublisher, 1, 1, 1, 1)
        self.checkPublishCity = QtWidgets.QCheckBox(self.tab_2)
        self.checkPublishCity.setObjectName("checkPublishCity")
        self.gridLayout_2.addWidget(self.checkPublishCity, 2, 0, 1, 1)
        self.textPublishCity = QtWidgets.QLineEdit(self.tab_2)
        self.textPublishCity.setObjectName("textPublishCity")
        self.gridLayout_2.addWidget(self.textPublishCity, 2, 1, 1, 1)
        self.checkPublishYear = QtWidgets.QCheckBox(self.tab_2)
        self.checkPublishYear.setObjectName("checkPublishYear")
        self.gridLayout_2.addWidget(self.checkPublishYear, 3, 0, 1, 1)
        self.textPublishYear = QtWidgets.QLineEdit(self.tab_2)
        self.textPublishYear.setMaximumSize(QtCore.QSize(50, 16777215))
        self.textPublishYear.setObjectName("textPublishYear")
        self.gridLayout_2.addWidget(self.textPublishYear, 3, 1, 1, 1)
        self.checkPublishISBN = QtWidgets.QCheckBox(self.tab_2)
        self.checkPublishISBN.setObjectName("checkPublishISBN")
        self.gridLayout_2.addWidget(self.checkPublishISBN, 4, 0, 1, 1)
        self.textPublishISBN = QtWidgets.QLineEdit(self.tab_2)
        self.textPublishISBN.setObjectName("textPublishISBN")
        self.gridLayout_2.addWidget(self.textPublishISBN, 4, 1, 1, 1)
        self.checkPublishSeries = QtWidgets.QCheckBox(self.tab_2)
        self.checkPublishSeries.setObjectName("checkPublishSeries")
        self.gridLayout_2.addWidget(self.checkPublishSeries, 5, 0, 1, 1)
        self.textPublishSeries = QtWidgets.QLineEdit(self.tab_2)
        self.textPublishSeries.setObjectName("textPublishSeries")
        self.gridLayout_2.addWidget(self.textPublishSeries, 5, 1, 1, 1)
        self.checkPublishSeriesIndex = QtWidgets.QCheckBox(self.tab_2)
        self.checkPublishSeriesIndex.setObjectName("checkPublishSeriesIndex")
        self.gridLayout_2.addWidget(self.checkPublishSeriesIndex, 6, 0, 1, 1)
        self.textPublishSeriesIndex = QtWidgets.QLineEdit(self.tab_2)
        self.textPublishSeriesIndex.setMaximumSize(QtCore.QSize(50, 16777215))
        self.textPublishSeriesIndex.setObjectName("textPublishSeriesIndex")
        self.gridLayout_2.addWidget(self.textPublishSeriesIndex, 6, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 76, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 7, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(EditDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(EditDialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.rejected.connect(EditDialog.reject)
        self.buttonBox.accepted.connect(EditDialog.accept)
        self.btnLoadFromFile.clicked.connect(EditDialog.onBtnLoadClick)
        self.btnSaveToFile.clicked.connect(EditDialog.onBtnSaveClick)
        QtCore.QMetaObject.connectSlotsByName(EditDialog)

    def retranslateUi(self, EditDialog):
        _translate = QtCore.QCoreApplication.translate
        EditDialog.setWindowTitle(_translate("EditDialog", "Edit"))
        self.cover.setText(_translate("EditDialog", "NO COVER ART"))
        self.btnLoadFromFile.setText(_translate("EditDialog", "Load from file"))
        self.btnSaveToFile.setText(_translate("EditDialog", "Save to file"))
        self.checkTitle.setText(_translate("EditDialog", "Title"))
        self.checkAuthor.setText(_translate("EditDialog", "Author"))
        self.checkSeries.setText(_translate("EditDialog", "Series"))
        self.checkSeriesIndex.setText(_translate("EditDialog", "Series index"))
        self.checkTags.setText(_translate("EditDialog", "Tags (genres)"))
        self.checkLang.setText(_translate("EditDialog", "Lang"))
        self.checkTranslator.setText(_translate("EditDialog", "Translator"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("EditDialog", "Basic info"))
        self.checkPublishTitle.setText(_translate("EditDialog", "Title"))
        self.checkPublishPublisher.setText(_translate("EditDialog", "Publisher"))
        self.checkPublishCity.setText(_translate("EditDialog", "City"))
        self.checkPublishYear.setText(_translate("EditDialog", "Year"))
        self.checkPublishISBN.setText(_translate("EditDialog", "ISBN"))
        self.checkPublishSeries.setText(_translate("EditDialog", "Series"))
        self.checkPublishSeriesIndex.setText(_translate("EditDialog", "Series index"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("EditDialog", "Publish info"))
from .customcontrols import ButtonLineEdit
