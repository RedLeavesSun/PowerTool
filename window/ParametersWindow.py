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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QWidget)

from util import util

from ui.Ui_ParametersWindow import Ui_ParametersWindow


class ParametersWindow(QMainWindow, Ui_ParametersWindow):
    def __init__(self, context):
        QMainWindow.__init__(self)
        Ui_ParametersWindow.__init__(self)

        self.context = context

        self.setupUi(self)
        util.centerWindow(self)

        self.sliPowerUpTime.valueChanged.connect(self.onSliPowerUpTimeValueChanged)
        self.sliPowerUpCurrentLimit.valueChanged.connect(self.onSliPowerUpCurrentLimitValueChanged)
        self.sliRunTimeCurrentLimit.valueChanged.connect(self.onSliRunTimeCurrentLimitValueChanged)
        self.sliFanTempLimit.valueChanged.connect(self.onSliFanTempLimitValueChanged)

        self.btnPowerUpTimeDefault.clicked.connect(self.onBtnPowerUpTimeDefaultClicked)
        self.btnPowerUpCurrentLimitDefault.clicked.connect(self.onBtnPowerUpCurrentLimitDefaultClicked)
        self.btnRunTimeCurrentLimitDefault.clicked.connect(self.onBtnRunTimeCurrentLimitDefaultClicked)
        self.btnTempDirectoryDefault.clicked.connect(self.onTempDirectoryDefaultClicked)
        self.btnEnableDeviceScanningDefault.clicked.connect(self.onEnableDeviceScanningDefaultClicked)
        self.btnFanTempLimitDefault.clicked.connect(self.onFanTempLimitDefaultClicked)

        self.btnRefresh.clicked.connect(self.onBtnRefreshClicked)
        self.btnDefaults.clicked.connect(self.onBtnDefaultsClicked)
        self.btnApply.clicked.connect(self.onBtnApplyClicked)
        self.btnClose.clicked.connect(self.onBtnCloseClicked)


    def setMonsoon(self, monsoon):
        self.monsoon = monsoon


    @Slot()
    def onSliPowerUpTimeValueChanged(self, value):
        self.powerUpTime = value
        self.labPowerUpTime.setText(str(self.powerUpTime))


    @Slot()
    def onSliPowerUpCurrentLimitValueChanged(self, value):
        self.powerUpCurrentLimit = value / 1000
        self.labPowerUpCurrentLimit.setText(str(self.powerUpCurrentLimit))



    @Slot()
    def onSliRunTimeCurrentLimitValueChanged(self, value):
        self.runTimeCurrentLimit = value / 1000
        self.labRunTimeCurrentLimit.setText(str(self.runTimeCurrentLimit))


    @Slot()
    def onSliFanTempLimitValueChanged(self, value):
        self.fanTempLimit = value
        self.labFanTempLimit.setText(str(self.fanTempLimit))


    @Slot()
    def onBtnPowerUpTimeDefaultClicked(self):
        pass


    @Slot()
    def onBtnPowerUpCurrentLimitDefaultClicked(self):
        pass


    @Slot()
    def onBtnRunTimeCurrentLimitDefaultClicked(self):
        pass


    @Slot()
    def onTempDirectoryDefaultClicked(self):
        pass


    @Slot()
    def onEnableDeviceScanningDefaultClicked(self):
        pass


    @Slot()
    def onFanTempLimitDefaultClicked(self):
        pass


    @Slot()
    def onBtnRefreshClicked(self):
        pass


    @Slot()
    def onBtnDefaultsClicked(self):
        self.btnPowerUpTimeDefault.click()
        self.btnPowerUpCurrentLimitDefault.click()
        self.btnRunTimeCurrentLimitDefault.click()
        self.btnTempDirectoryDefault.click()
        self.btnEnableDeviceScanningDefault.click()
        self.btnFanTempLimitDefault.click()


    @Slot()
    def onBtnApplyClicked(self):
        self.monsoon.setPowerupTime(self.powerUpTime)
        self.monsoon.setPowerUpCurrentLimit(self.powerUpCurrentLimit)
        self.monsoon.setRunTimeCurrentLimit(self.runTimeCurrentLimit)
        self.monsoon.setTemperatureLimit(self.fanTempLimit)


    @Slot()
    def onBtnCloseClicked(self):
        self.close()
