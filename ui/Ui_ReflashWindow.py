# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_ReflashWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QWidget)

class Ui_ReflashWindow(object):
    def setupUi(self, ReflashWindow):
        if not ReflashWindow.objectName():
            ReflashWindow.setObjectName(u"ReflashWindow")
        ReflashWindow.resize(392, 280)
        self.centralwidget = QWidget(ReflashWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(8, 8, 185, 89))
        self.btnReflash = QPushButton(self.groupBox)
        self.btnReflash.setObjectName(u"btnReflash")
        self.btnReflash.setGeometry(QRect(8, 32, 169, 49))
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(200, 8, 185, 89))
        self.progStatus = QProgressBar(self.groupBox_2)
        self.progStatus.setObjectName(u"progStatus")
        self.progStatus.setGeometry(QRect(8, 56, 169, 23))
        self.progStatus.setValue(0)
        self.labStatus = QLabel(self.groupBox_2)
        self.labStatus.setObjectName(u"labStatus")
        self.labStatus.setGeometry(QRect(8, 32, 67, 17))
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(8, 104, 377, 80))
        self.labHardwareInformation = QLabel(self.groupBox_3)
        self.labHardwareInformation.setObjectName(u"labHardwareInformation")
        self.labHardwareInformation.setGeometry(QRect(8, 24, 361, 17))
        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(8, 192, 377, 80))
        self.labRecommended = QLabel(self.groupBox_4)
        self.labRecommended.setObjectName(u"labRecommended")
        self.labRecommended.setGeometry(QRect(8, 24, 361, 17))
        ReflashWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ReflashWindow)

        QMetaObject.connectSlotsByName(ReflashWindow)
    # setupUi

    def retranslateUi(self, ReflashWindow):
        ReflashWindow.setWindowTitle(QCoreApplication.translate("ReflashWindow", u"PMFlashWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("ReflashWindow", u"Hex file", None))
        self.btnReflash.setText(QCoreApplication.translate("ReflashWindow", u"Reflash", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("ReflashWindow", u"Status", None))
        self.labStatus.setText(QCoreApplication.translate("ReflashWindow", u"Idle", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("ReflashWindow", u"Hardware Information", None))
        self.labHardwareInformation.setText(QCoreApplication.translate("ReflashWindow", u"TextLabel", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("ReflashWindow", u"Recommended", None))
        self.labRecommended.setText(QCoreApplication.translate("ReflashWindow", u"TextLabel", None))
    # retranslateUi

