# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SelectDeviceWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_SelectDeviceWindow(object):
    def setupUi(self, SelectDeviceWindow):
        if not SelectDeviceWindow.objectName():
            SelectDeviceWindow.setObjectName(u"SelectDeviceWindow")
        SelectDeviceWindow.resize(271, 296)
        font = QFont()
        font.setPointSize(10)
        SelectDeviceWindow.setFont(font)
        self.centralwidget = QWidget(SelectDeviceWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnRefresh = QPushButton(self.centralwidget)
        self.btnRefresh.setObjectName(u"btnRefresh")
        self.btnRefresh.setGeometry(QRect(176, 40, 89, 25))
        self.btnViewOnly = QPushButton(self.centralwidget)
        self.btnViewOnly.setObjectName(u"btnViewOnly")
        self.btnViewOnly.setGeometry(QRect(176, 72, 89, 25))
        self.btnExit = QPushButton(self.centralwidget)
        self.btnExit.setObjectName(u"btnExit")
        self.btnExit.setGeometry(QRect(176, 104, 89, 25))
        self.btnSelect = QPushButton(self.centralwidget)
        self.btnSelect.setObjectName(u"btnSelect")
        self.btnSelect.setGeometry(QRect(176, 8, 90, 25))
        self.btnReflash = QPushButton(self.centralwidget)
        self.btnReflash.setObjectName(u"btnReflash")
        self.btnReflash.setGeometry(QRect(176, 264, 89, 25))
        self.lvDevices = QListWidget(self.centralwidget)
        self.lvDevices.setObjectName(u"lvDevices")
        self.lvDevices.setGeometry(QRect(8, 8, 161, 281))
        SelectDeviceWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SelectDeviceWindow)

        QMetaObject.connectSlotsByName(SelectDeviceWindow)
    # setupUi

    def retranslateUi(self, SelectDeviceWindow):
        SelectDeviceWindow.setWindowTitle(QCoreApplication.translate("SelectDeviceWindow", u"Please select a device", None))
        self.btnRefresh.setText(QCoreApplication.translate("SelectDeviceWindow", u"Refresh", None))
        self.btnViewOnly.setText(QCoreApplication.translate("SelectDeviceWindow", u"View Only", None))
        self.btnExit.setText(QCoreApplication.translate("SelectDeviceWindow", u"Exit", None))
        self.btnSelect.setText(QCoreApplication.translate("SelectDeviceWindow", u"Select", None))
        self.btnReflash.setText(QCoreApplication.translate("SelectDeviceWindow", u"Reflash", None))
    # retranslateUi

