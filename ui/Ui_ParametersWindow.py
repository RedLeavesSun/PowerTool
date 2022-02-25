# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_ParametersWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QSlider, QWidget)

class Ui_ParametersWindow(object):
    def setupUi(self, ParametersWindow):
        if not ParametersWindow.objectName():
            ParametersWindow.setObjectName(u"ParametersWindow")
        ParametersWindow.resize(600, 440)
        font = QFont()
        font.setPointSize(10)
        ParametersWindow.setFont(font)
        self.centralwidget = QWidget(ParametersWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(8, 8, 289, 57))
        self.labPowerUpTime = QLabel(self.groupBox)
        self.labPowerUpTime.setObjectName(u"labPowerUpTime")
        self.labPowerUpTime.setGeometry(QRect(8, 32, 67, 17))
        self.labPowerUpTime.setFont(font)
        self.labPowerUpTime.setStyleSheet(u"border: 1px solid black;")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 32, 25, 17))
        self.sliPowerUpTime = QSlider(self.groupBox)
        self.sliPowerUpTime.setObjectName(u"sliPowerUpTime")
        self.sliPowerUpTime.setGeometry(QRect(112, 32, 105, 16))
        self.sliPowerUpTime.setMaximum(255)
        self.sliPowerUpTime.setOrientation(Qt.Horizontal)
        self.btnPowerUpTimeDefault = QPushButton(self.groupBox)
        self.btnPowerUpTimeDefault.setObjectName(u"btnPowerUpTimeDefault")
        self.btnPowerUpTimeDefault.setGeometry(QRect(224, 24, 57, 25))
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(8, 72, 289, 57))
        self.labPowerUpCurrentLimit = QLabel(self.groupBox_2)
        self.labPowerUpCurrentLimit.setObjectName(u"labPowerUpCurrentLimit")
        self.labPowerUpCurrentLimit.setGeometry(QRect(8, 32, 67, 17))
        self.labPowerUpCurrentLimit.setStyleSheet(u"border: 1px solid black;")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(80, 32, 25, 17))
        self.sliPowerUpCurrentLimit = QSlider(self.groupBox_2)
        self.sliPowerUpCurrentLimit.setObjectName(u"sliPowerUpCurrentLimit")
        self.sliPowerUpCurrentLimit.setGeometry(QRect(112, 32, 105, 16))
        self.sliPowerUpCurrentLimit.setMaximum(15625)
        self.sliPowerUpCurrentLimit.setOrientation(Qt.Horizontal)
        self.btnPowerUpCurrentLimitDefault = QPushButton(self.groupBox_2)
        self.btnPowerUpCurrentLimitDefault.setObjectName(u"btnPowerUpCurrentLimitDefault")
        self.btnPowerUpCurrentLimitDefault.setGeometry(QRect(224, 24, 57, 25))
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(8, 136, 289, 57))
        self.labRunTimeCurrentLimit = QLabel(self.groupBox_3)
        self.labRunTimeCurrentLimit.setObjectName(u"labRunTimeCurrentLimit")
        self.labRunTimeCurrentLimit.setGeometry(QRect(8, 32, 67, 17))
        self.labRunTimeCurrentLimit.setStyleSheet(u"border: 1px solid black;")
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(80, 32, 25, 17))
        self.sliRunTimeCurrentLimit = QSlider(self.groupBox_3)
        self.sliRunTimeCurrentLimit.setObjectName(u"sliRunTimeCurrentLimit")
        self.sliRunTimeCurrentLimit.setGeometry(QRect(112, 32, 105, 16))
        self.sliRunTimeCurrentLimit.setMaximum(15625)
        self.sliRunTimeCurrentLimit.setOrientation(Qt.Horizontal)
        self.btnRunTimeCurrentLimitDefault = QPushButton(self.groupBox_3)
        self.btnRunTimeCurrentLimitDefault.setObjectName(u"btnRunTimeCurrentLimitDefault")
        self.btnRunTimeCurrentLimitDefault.setGeometry(QRect(224, 24, 57, 25))
        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(8, 200, 289, 57))
        self.btnTempDirectoryDefault = QPushButton(self.groupBox_4)
        self.btnTempDirectoryDefault.setObjectName(u"btnTempDirectoryDefault")
        self.btnTempDirectoryDefault.setGeometry(QRect(224, 24, 57, 25))
        self.lineEdit = QLineEdit(self.groupBox_4)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(8, 24, 177, 25))
        self.pushButton_11 = QPushButton(self.groupBox_4)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(192, 24, 25, 25))
        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(8, 392, 585, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btnRefresh = QPushButton(self.horizontalLayoutWidget_2)
        self.btnRefresh.setObjectName(u"btnRefresh")

        self.horizontalLayout_2.addWidget(self.btnRefresh)

        self.btnDefaults = QPushButton(self.horizontalLayoutWidget_2)
        self.btnDefaults.setObjectName(u"btnDefaults")

        self.horizontalLayout_2.addWidget(self.btnDefaults)

        self.btnApply = QPushButton(self.horizontalLayoutWidget_2)
        self.btnApply.setObjectName(u"btnApply")

        self.horizontalLayout_2.addWidget(self.btnApply)

        self.btnClose = QPushButton(self.horizontalLayoutWidget_2)
        self.btnClose.setObjectName(u"btnClose")

        self.horizontalLayout_2.addWidget(self.btnClose)

        self.groupBox_6 = QGroupBox(self.centralwidget)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(8, 328, 289, 57))
        self.labFanTempLimit = QLabel(self.groupBox_6)
        self.labFanTempLimit.setObjectName(u"labFanTempLimit")
        self.labFanTempLimit.setGeometry(QRect(8, 32, 67, 17))
        self.labFanTempLimit.setStyleSheet(u"border: 1px solid black;")
        self.label_10 = QLabel(self.groupBox_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(80, 32, 33, 17))
        self.sliFanTempLimit = QSlider(self.groupBox_6)
        self.sliFanTempLimit.setObjectName(u"sliFanTempLimit")
        self.sliFanTempLimit.setGeometry(QRect(112, 32, 105, 16))
        self.sliFanTempLimit.setMinimum(1)
        self.sliFanTempLimit.setMaximum(60)
        self.sliFanTempLimit.setOrientation(Qt.Horizontal)
        self.btnFanTempLimitDefault = QPushButton(self.groupBox_6)
        self.btnFanTempLimitDefault.setObjectName(u"btnFanTempLimitDefault")
        self.btnFanTempLimitDefault.setGeometry(QRect(224, 24, 57, 25))
        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(8, 264, 289, 57))
        self.btnEnableDeviceScanningDefault = QPushButton(self.groupBox_5)
        self.btnEnableDeviceScanningDefault.setObjectName(u"btnEnableDeviceScanningDefault")
        self.btnEnableDeviceScanningDefault.setGeometry(QRect(224, 24, 57, 25))
        self.horizontalLayoutWidget_3 = QWidget(self.groupBox_5)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(8, 24, 209, 25))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.radioButton_3 = QRadioButton(self.horizontalLayoutWidget_3)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setChecked(True)

        self.horizontalLayout_3.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.horizontalLayoutWidget_3)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.horizontalLayout_3.addWidget(self.radioButton_4)

        ParametersWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ParametersWindow)

        QMetaObject.connectSlotsByName(ParametersWindow)
    # setupUi

    def retranslateUi(self, ParametersWindow):
        ParametersWindow.setWindowTitle(QCoreApplication.translate("ParametersWindow", u"Set Parameters", None))
        self.groupBox.setTitle(QCoreApplication.translate("ParametersWindow", u"Power-up time", None))
        self.labPowerUpTime.setText(QCoreApplication.translate("ParametersWindow", u"0", None))
        self.label_3.setText(QCoreApplication.translate("ParametersWindow", u"ms", None))
        self.btnPowerUpTimeDefault.setText(QCoreApplication.translate("ParametersWindow", u"Default", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("ParametersWindow", u"Power-up current limit", None))
        self.labPowerUpCurrentLimit.setText(QCoreApplication.translate("ParametersWindow", u"0", None))
        self.label_4.setText(QCoreApplication.translate("ParametersWindow", u"A", None))
        self.btnPowerUpCurrentLimitDefault.setText(QCoreApplication.translate("ParametersWindow", u"Default", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("ParametersWindow", u"Run-time current limit", None))
        self.labRunTimeCurrentLimit.setText(QCoreApplication.translate("ParametersWindow", u"0", None))
        self.label_6.setText(QCoreApplication.translate("ParametersWindow", u"A", None))
        self.btnRunTimeCurrentLimitDefault.setText(QCoreApplication.translate("ParametersWindow", u"Default", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("ParametersWindow", u"Temp Directory", None))
        self.btnTempDirectoryDefault.setText(QCoreApplication.translate("ParametersWindow", u"Default", None))
        self.pushButton_11.setText(QCoreApplication.translate("ParametersWindow", u"...", None))
        self.btnRefresh.setText(QCoreApplication.translate("ParametersWindow", u"Refresh", None))
        self.btnDefaults.setText(QCoreApplication.translate("ParametersWindow", u"Defaults", None))
        self.btnApply.setText(QCoreApplication.translate("ParametersWindow", u"Apply", None))
        self.btnClose.setText(QCoreApplication.translate("ParametersWindow", u"Close", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("ParametersWindow", u"Fan Temp Limit", None))
        self.labFanTempLimit.setText(QCoreApplication.translate("ParametersWindow", u"0", None))
        self.label_10.setText(QCoreApplication.translate("ParametersWindow", u"Deg", None))
        self.btnFanTempLimitDefault.setText(QCoreApplication.translate("ParametersWindow", u"Default", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("ParametersWindow", u"Enable Device Scanning", None))
        self.btnEnableDeviceScanningDefault.setText(QCoreApplication.translate("ParametersWindow", u"Default", None))
        self.radioButton_3.setText(QCoreApplication.translate("ParametersWindow", u"On", None))
        self.radioButton_4.setText(QCoreApplication.translate("ParametersWindow", u"Off", None))
    # retranslateUi

