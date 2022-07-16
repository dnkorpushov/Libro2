# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src\designer\bookinfopanel.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BookInfoPanel(object):
    def setupUi(self, BookInfoPanel):
        BookInfoPanel.setObjectName("BookInfoPanel")
        BookInfoPanel.resize(200, 770)
        BookInfoPanel.setMinimumSize(QtCore.QSize(200, 0))
        BookInfoPanel.setBaseSize(QtCore.QSize(200, 0))
        BookInfoPanel.setFocusPolicy(QtCore.Qt.StrongFocus)
        BookInfoPanel.setStyleSheet("QWidget { background-color #f7f7f7\n"
" }r")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(BookInfoPanel)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(BookInfoPanel)
        self.scrollArea.setMinimumSize(QtCore.QSize(200, 0))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 210, 749))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.toggleMainInfo = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleMainInfo.sizePolicy().hasHeightForWidth())
        self.toggleMainInfo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.toggleMainInfo.setFont(font)
        self.toggleMainInfo.setStyleSheet("QToolButton { border: none }")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/expanded_12px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toggleMainInfo.setIcon(icon)
        self.toggleMainInfo.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toggleMainInfo.setAutoRaise(False)
        self.toggleMainInfo.setArrowType(QtCore.Qt.NoArrow)
        self.toggleMainInfo.setObjectName("toggleMainInfo")
        self.verticalLayout.addWidget(self.toggleMainInfo)
        self.widgetMain = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widgetMain.setMinimumSize(QtCore.QSize(200, 0))
        self.widgetMain.setObjectName("widgetMain")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widgetMain)
        self.verticalLayout_4.setContentsMargins(10, 0, 6, 10)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.widgetMain)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.textTitle = ComboEdit(self.widgetMain)
        self.textTitle.setObjectName("textTitle")
        self.verticalLayout_4.addWidget(self.textTitle)
        self.label_3 = QtWidgets.QLabel(self.widgetMain)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.textAuthor = ComboEdit(self.widgetMain)
        self.textAuthor.setObjectName("textAuthor")
        self.verticalLayout_4.addWidget(self.textAuthor)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(4)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.widgetMain)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.widgetMain)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.textSeries = ComboEdit(self.widgetMain)
        self.textSeries.setObjectName("textSeries")
        self.gridLayout.addWidget(self.textSeries, 1, 0, 1, 1)
        self.textNumber = ComboEdit(self.widgetMain)
        self.textNumber.setMinimumSize(QtCore.QSize(20, 0))
        self.textNumber.setMaximumSize(QtCore.QSize(80, 16777215))
        self.textNumber.setBaseSize(QtCore.QSize(40, 0))
        self.textNumber.setObjectName("textNumber")
        self.gridLayout.addWidget(self.textNumber, 1, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.label_8 = QtWidgets.QLabel(self.widgetMain)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textTag = ComboEdit(self.widgetMain)
        self.textTag.setObjectName("textTag")
        self.horizontalLayout_2.addWidget(self.textTag)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.label_6 = QtWidgets.QLabel(self.widgetMain)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.textLang = ComboEdit(self.widgetMain)
        self.textLang.setObjectName("textLang")
        self.verticalLayout_4.addWidget(self.textLang)
        self.label_7 = QtWidgets.QLabel(self.widgetMain)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.textTranslator = ComboEdit(self.widgetMain)
        self.textTranslator.setObjectName("textTranslator")
        self.verticalLayout_4.addWidget(self.textTranslator)
        self.verticalLayout.addWidget(self.widgetMain)
        self.togglePublishInfo = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.togglePublishInfo.sizePolicy().hasHeightForWidth())
        self.togglePublishInfo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.togglePublishInfo.setFont(font)
        self.togglePublishInfo.setStyleSheet("QToolButton { border: none }")
        self.togglePublishInfo.setIcon(icon)
        self.togglePublishInfo.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.togglePublishInfo.setAutoRaise(False)
        self.togglePublishInfo.setObjectName("togglePublishInfo")
        self.verticalLayout.addWidget(self.togglePublishInfo)
        self.widgetPublishInfo = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widgetPublishInfo.setMinimumSize(QtCore.QSize(200, 0))
        self.widgetPublishInfo.setObjectName("widgetPublishInfo")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widgetPublishInfo)
        self.verticalLayout_5.setContentsMargins(10, 0, 6, 10)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.widgetPublishInfo)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.textPublishTitle = ComboEdit(self.widgetPublishInfo)
        self.textPublishTitle.setObjectName("textPublishTitle")
        self.verticalLayout_5.addWidget(self.textPublishTitle)
        self.label_9 = QtWidgets.QLabel(self.widgetPublishInfo)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.textPublishPublisher = ComboEdit(self.widgetPublishInfo)
        self.textPublishPublisher.setObjectName("textPublishPublisher")
        self.verticalLayout_5.addWidget(self.textPublishPublisher)
        self.label_10 = QtWidgets.QLabel(self.widgetPublishInfo)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_5.addWidget(self.label_10)
        self.textPublishCity = ComboEdit(self.widgetPublishInfo)
        self.textPublishCity.setObjectName("textPublishCity")
        self.verticalLayout_5.addWidget(self.textPublishCity)
        self.label_11 = QtWidgets.QLabel(self.widgetPublishInfo)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_5.addWidget(self.label_11)
        self.textPublishYear = ComboEdit(self.widgetPublishInfo)
        self.textPublishYear.setObjectName("textPublishYear")
        self.verticalLayout_5.addWidget(self.textPublishYear)
        self.label_12 = QtWidgets.QLabel(self.widgetPublishInfo)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_5.addWidget(self.label_12)
        self.textPublishISBN = ComboEdit(self.widgetPublishInfo)
        self.textPublishISBN.setObjectName("textPublishISBN")
        self.verticalLayout_5.addWidget(self.textPublishISBN)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_14 = QtWidgets.QLabel(self.widgetPublishInfo)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 0, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.widgetPublishInfo)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 0, 0, 1, 1)
        self.textPublishSeries = ComboEdit(self.widgetPublishInfo)
        self.textPublishSeries.setObjectName("textPublishSeries")
        self.gridLayout_2.addWidget(self.textPublishSeries, 1, 0, 1, 1)
        self.textPublishSeriesIndex = ComboEdit(self.widgetPublishInfo)
        self.textPublishSeriesIndex.setMinimumSize(QtCore.QSize(100, 0))
        self.textPublishSeriesIndex.setObjectName("textPublishSeriesIndex")
        self.gridLayout_2.addWidget(self.textPublishSeriesIndex, 1, 2, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_2)
        self.verticalLayout.addWidget(self.widgetPublishInfo)
        self.toggleCoverInfo = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleCoverInfo.sizePolicy().hasHeightForWidth())
        self.toggleCoverInfo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.toggleCoverInfo.setFont(font)
        self.toggleCoverInfo.setStyleSheet("QToolButton { border: none }")
        self.toggleCoverInfo.setIcon(icon)
        self.toggleCoverInfo.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toggleCoverInfo.setObjectName("toggleCoverInfo")
        self.verticalLayout.addWidget(self.toggleCoverInfo)
        self.widgetCoverInfo = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widgetCoverInfo.setMinimumSize(QtCore.QSize(200, 0))
        self.widgetCoverInfo.setObjectName("widgetCoverInfo")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widgetCoverInfo)
        self.verticalLayout_2.setContentsMargins(10, 0, 6, 10)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelCoverImage = QtWidgets.QLabel(self.widgetCoverInfo)
        self.labelCoverImage.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelCoverImage.setFont(font)
        self.labelCoverImage.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labelCoverImage.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelCoverImage.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCoverImage.setWordWrap(True)
        self.labelCoverImage.setObjectName("labelCoverImage")
        self.horizontalLayout.addWidget(self.labelCoverImage)
        self.labelImageInfo = QtWidgets.QLabel(self.widgetCoverInfo)
        self.labelImageInfo.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.labelImageInfo.setObjectName("labelImageInfo")
        self.horizontalLayout.addWidget(self.labelImageInfo)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.widgetCoverInfo)
        self.toggleDescription = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleDescription.sizePolicy().hasHeightForWidth())
        self.toggleDescription.setSizePolicy(sizePolicy)
        self.toggleDescription.setStyleSheet("QToolButton { border: none }")
        self.toggleDescription.setIcon(icon)
        self.toggleDescription.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toggleDescription.setObjectName("toggleDescription")
        self.verticalLayout.addWidget(self.toggleDescription)
        self.widgetDescriptionInfo = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widgetDescriptionInfo.setMinimumSize(QtCore.QSize(200, 0))
        self.widgetDescriptionInfo.setObjectName("widgetDescriptionInfo")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widgetDescriptionInfo)
        self.verticalLayout_7.setContentsMargins(10, 0, 6, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.textDescription = QtWidgets.QLabel(self.widgetDescriptionInfo)
        self.textDescription.setText("")
        self.textDescription.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.textDescription.setWordWrap(True)
        self.textDescription.setObjectName("textDescription")
        self.verticalLayout_7.addWidget(self.textDescription)
        self.verticalLayout.addWidget(self.widgetDescriptionInfo)
        spacerItem = QtWidgets.QSpacerItem(2, 2, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_6.addLayout(self.verticalLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)

        self.retranslateUi(BookInfoPanel)
        self.toggleMainInfo.clicked.connect(BookInfoPanel.onMainInfoToggle)
        self.toggleCoverInfo.clicked.connect(BookInfoPanel.onCoverInfoToggle)
        self.togglePublishInfo.clicked.connect(BookInfoPanel.onPublishInfoToggle)
        self.toggleDescription.clicked.connect(BookInfoPanel.onDescriptionInfoToggle)
        QtCore.QMetaObject.connectSlotsByName(BookInfoPanel)

    def retranslateUi(self, BookInfoPanel):
        _translate = QtCore.QCoreApplication.translate
        BookInfoPanel.setWindowTitle(_translate("BookInfoPanel", "Form"))
        self.toggleMainInfo.setText(_translate("BookInfoPanel", "Main information"))
        self.label_2.setText(_translate("BookInfoPanel", "Title"))
        self.label_3.setText(_translate("BookInfoPanel", "Author"))
        self.label_4.setText(_translate("BookInfoPanel", "Number"))
        self.label.setText(_translate("BookInfoPanel", "Series"))
        self.label_8.setText(_translate("BookInfoPanel", "Tags (genres)"))
        self.label_6.setText(_translate("BookInfoPanel", "Lang"))
        self.label_7.setText(_translate("BookInfoPanel", "Translator"))
        self.togglePublishInfo.setText(_translate("BookInfoPanel", "Publish information"))
        self.label_5.setText(_translate("BookInfoPanel", "Title"))
        self.label_9.setText(_translate("BookInfoPanel", "Publisher"))
        self.label_10.setText(_translate("BookInfoPanel", "City"))
        self.label_11.setText(_translate("BookInfoPanel", "Year"))
        self.label_12.setText(_translate("BookInfoPanel", "ISBN"))
        self.label_14.setText(_translate("BookInfoPanel", "Number"))
        self.label_15.setText(_translate("BookInfoPanel", "Series"))
        self.toggleCoverInfo.setText(_translate("BookInfoPanel", "Cover"))
        self.labelCoverImage.setText(_translate("BookInfoPanel", "No cover image"))
        self.labelImageInfo.setText(_translate("BookInfoPanel", "image/jpeg\n"
"0x0\n"
"0 KB"))
        self.toggleDescription.setText(_translate("BookInfoPanel", "Description"))
from .comboedit import ComboEdit
from . import resources_rc
