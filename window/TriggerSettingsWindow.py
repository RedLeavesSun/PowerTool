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

from ui.Ui_TriggerSettingsWindow import Ui_TriggerSettingsWindow


class TriggerSettingsWindow(QMainWindow, Ui_TriggerSettingsWindow):
    def __init__(self, context):
        QMainWindow.__init__(self)
        Ui_TriggerSettingsWindow.__init__(self)

        self.context = context

        self.setupUi(self)
        util.centerWindow(self)


    def setMonsoon(self, monsoon):
        self.monsoon = monsoon
