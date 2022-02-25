#!/usr/bin/python3
# -*- coding=utf-8 -*-
# author:   RedLeaves
# date:     2022/02/25
# version:  1.0


from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtCore import (Slot, Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtGui import (QGuiApplication)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QWidget)
from PySide6.QtWidgets import (QListWidgetItem)

from util import util

from ui.Ui_SelectDeviceWindow import Ui_SelectDeviceWindow

class SelectDeviceWindow(QMainWindow, Ui_SelectDeviceWindow):
    def __init__(self, context):
        QMainWindow.__init__(self)
        Ui_SelectDeviceWindow.__init__(self)

        self.context = context

        self.setupUi(self)
        util.centerWindow(self)

        self.btnSelect.clicked.connect(self.onBtnSelectClicked)
        self.btnRefresh.clicked.connect(self.onBtnRefreshClicked)
        self.btnViewOnly.clicked.connect(self.onBtnViewOnlyClicked)
        self.btnExit.clicked.connect(self.onBtnExitClicked)
        self.btnReflash.clicked.connect(self.onBtnReflashClicked)

        self.lvDevices.currentTextChanged.connect(self.onLvDevicesCurrentChanged)


    def setMainWindow(self, mainWindow):
        self.mainWindow = mainWindow


    def setReflashWindow(self, reflashWindow):
        self.reflashWindow = reflashWindow


    def setMonsoon(self, monsoon):
        self.monsoon = monsoon


    @Slot()
    def onBtnSelectClicked(self):
        print("onBtnSelectClicked")

        if self.serialNumber == None:
            return

        self.monsoon.setup_usb(self.serialNumber)
        self.monsoon.fillStatusPacket()

        self.mainWindow.show()
        self.close()


    @Slot()
    def onBtnRefreshClicked(self):
        print("onBtnRefreshClicked")
        self.lvDevices.clear()
        serialNumbers = self.monsoon.enumerateDevices()
        for serialNumber in serialNumbers:
            self.lvDevices.addItem(QListWidgetItem(serialNumber))


    @Slot()
    def onBtnViewOnlyClicked(self):
        print("onBtnViewOnlyClicked")
        self.mainWindow.show()
        self.close()


    @Slot()
    def onBtnExitClicked(self):
        print("onBtnExitClicked")
        exit()


    @Slot()
    def onBtnReflashClicked(self):
        print("onBtnReflashClicked")
        self.reflashWindow.show()
        self.close()


    @Slot()
    def onLvDevicesCurrentChanged(self, currentText):
        print("onLvDevicesCurrentChanged")
        self.serialNumber = currentText
