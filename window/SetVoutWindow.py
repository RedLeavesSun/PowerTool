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

from ui.Ui_SetVoutWindow import Ui_SetVoutWindow


class SetVoutWindow(QMainWindow, Ui_SetVoutWindow):
    def __init__(self, context):
        QMainWindow.__init__(self)
        Ui_SetVoutWindow.__init__(self)

        self.context = context

        self.setupUi(self)
        util.centerWindow(self)

        self.rbTypical.clicked.connect(self.onRbTypicalClicked)
        self.rbLow.clicked.connect(self.onRbLowClicked)
        self.rbHigh.clicked.connect(self.onRbHighClicked)
        self.rbDigtal.clicked.connect(self.onRbDigtalClicked)
        self.rbThreeCell.clicked.connect(self.onRbThreeCellClicked)
        self.rbCustom.clicked.connect(self.onRbCustomClicked)

        self.btnOk.clicked.connect(self.onBtnOkClicked)
        self.btnCancel.clicked.connect(self.onBtnCancelClicked)


    def setMonsoon(self, monsoon):
        self.monsoon = monsoon


    @Slot()
    def onRbTypicalClicked(self, checked):
        self.vout = 3.70


    @Slot()
    def onRbLowClicked(self, checked):
        self.vout = 3.35


    @Slot()
    def onRbHighClicked(self, checked):
        self.vout = 4.20


    @Slot()
    def onRbDigtalClicked(self, checked):
        self.vout = 5.00


    @Slot()
    def onRbThreeCellClicked(self, checked):
        self.vout = 11.10


    @Slot()
    def onRbCustomClicked(self, checked):
        self.vout(float(self.edCustom.text))


    @Slot()
    def onBtnOkClicked(self):
        self.context.vout = self.vout


    @Slot()
    def onBtnCancelClicked(self):
        self.close()
