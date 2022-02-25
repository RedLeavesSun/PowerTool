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
from PySide6.QtGui import (QPen)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QWidget)

from PySide6.QtCharts import (QChart, QLineSeries, QValueAxis)

from util import util

from ui.Ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, context):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)

        self.context = context

        self.setupUi(self)
        util.centerWindow(self)

        self.btnVoutSwitch.clicked.connect(self.onBtnVoutSwitchClicked)
        self.btnSetVout.clicked.connect(self.onBtnSetVoutClicked)

        self.btnSetCaptureTriggers.clicked.connect(self.onBtnSetCaptureTriggersClicked)

        self.btnRun.clicked.connect(self.onBtnRunClicked)
        self.btnStop.clicked.connect(self.onBtnStopClicked)

        self.btnReset.clicked.connect(self.onBtnResetClicked)

        self.btnOpen.clicked.connect(self.onBtnOpenClicked)
        self.btnSave.clicked.connect(self.onBtnSaveClicked)

        self.btnExport.clicked.connect(self.onBtnExportClicked)

        self.btnCopyGraph.clicked.connect(self.onBtnCopyGraphClicked)
        self.btnCoovStats.clicked.connect(self.onBtnCoovStatsClicked)
        self.btnCopyScreen.clicked.connect(self.onBtnCopyScreenClicked)

        self.btnParaments.clicked.connect(self.onBtnParamentsClicked)
        self.btnRestoreDefaults.clicked.connect(self.onBtnRestoreDefaultsClicked)

        font = QFont()
        font.setPointSize(8)

        pen = QPen()

        axisX = QValueAxis()
        axisY1 = QValueAxis()
        axisY2 = QValueAxis()

        axisX.setRange(0, 5)
        axisY1.setRange(0, 200)
        axisY2.setRange(0, 10)

        axisX.setLabelFormat("%d")
        axisY1.setLabelFormat("%d")
        axisY2.setLabelFormat("%d")

        axisX.setMinorTickCount(10)
        axisY1.setMinorTickCount(5)
        axisY2.setMinorTickCount(5)

        axisX.setLabelsFont(font)
        axisY1.setLabelsFont(font)
        axisY2.setLabelsFont(font)

        pen.setWidth(1)
        pen.setStyle(Qt.PenStyle.SolidLine)

        axisX.setLinePen(pen)
        axisY1.setLinePen(pen)
        axisY2.setLinePen(pen)

        pen.setWidth(1)
        pen.setStyle(Qt.PenStyle.DashLine)

        axisX.setGridLinePen(pen)
        axisY1.setGridLinePen(pen)
        axisY2.setGridLinePen(pen)

        pen.setWidth(1)
        pen.setStyle(Qt.PenStyle.DotLine)

        axisX.setMinorGridLinePen(pen)
        axisY1.setMinorGridLinePen(pen)
        axisY2.setMinorGridLinePen(pen)

        chart = QChart()
        chart.setBackgroundRoundness(0)
        chart.layout().setContentsMargins(0, 0, 0, 0)
        chart.legend().hide()
        chart.addAxis(axisX, Qt.AlignBottom)
        chart.addAxis(axisY1, Qt.AlignRight)
        chart.addAxis(axisY2, Qt.AlignRight)

        series = QLineSeries()

        for i in range(100):
            series.append(i, i)

        chart.addSeries(series)

        self.graphicsView.setChart(chart)


    def setMonsoon(self, monsoon):
        self.monsoon = monsoon


    def setSetVoutWindow(self, setVoutWindow):
        self.setVoutWindow = setVoutWindow


    def setParametersWindow(self, parametersWindow):
        self.parametersWindow = parametersWindow


    def setTriggerSettingsWindow(self, triggerSettingsWindow):
        self.triggerSettingsWindow = triggerSettingsWindow


    @Slot()
    def onBtnVoutSwitchClicked(self):
        print("onBtnVoutSwitchClicked")

        if self.context.voutSwitch != True:
            self.context.voutSwitch == True
        else:
            self.context.voutSwitch == False

        if self.context.voutSwitch == True:
            if self.context.vout != None:
                self.monsoon.setVout(self.context.vout)
        else:
            self.monsoon.setVout(0)


    @Slot()
    def onBtnSetVoutClicked(self):
        print("onBtnSetVoutClicked")

        self.setVoutWindow.show()


    @Slot()
    def onBtnSetCaptureTriggersClicked(self):
        print("onBtnSetCaptureTriggersClicked")
        self.triggerSettingsWindow.show()


    @Slot()
    def onBtnRunClicked(self):
        print("onBtnRunClicked")


    @Slot()
    def onBtnStopClicked(self):
        print("onBtnStopClicked")


    @Slot()
    def onBtnResetClicked(self):
        print("onBtnResetClicked")


    @Slot()
    def onBtnOpenClicked(self):
        print("onBtnOpenClicked")


    @Slot()
    def onBtnSaveClicked(self):
        print("onBtnSaveClicked")


    @Slot()
    def onBtnExportClicked(self):
        print("onBtnExportClicked")


    @Slot()
    def onBtnCopyGraphClicked(self):
        print("onBtnCopyGraphClicked")


    @Slot()
    def onBtnCoovStatsClicked(self):
        print("onBtnCoovStatsClicked")


    @Slot()
    def onBtnCopyScreenClicked(self):
        print("onBtnCopyScreenClicked")


    @Slot()
    def onBtnParamentsClicked(self):
        print("onBtnParamentsClicked")
        self.parametersWindow.show()


    @Slot()
    def onBtnRestoreDefaultsClicked(self):
        print("onBtnRestoreDefaultsClicked")
