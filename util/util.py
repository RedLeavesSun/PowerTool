#!/usr/bin/python3
# -*- coding=utf-8 -*-
# author:   RedLeaves
# date:     2022/02/25
# version:  1.0


from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtGui import (QGuiApplication)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QWidget)


def centerWindow(widget):
    primaryScreen = QGuiApplication.primaryScreen().geometry()
    primaryScreenX = primaryScreen.x()
    primaryScreenY = primaryScreen.y()
    primaryScreenWidth = primaryScreen.width()
    primaryScreenHeight = primaryScreen.height()
    windowX = (primaryScreenWidth - widget.width()) / 2 + primaryScreenX
    windowY = (primaryScreenHeight - widget.height()) / 2 + primaryScreenY
    widget.setGeometry(windowX, windowY, widget.width(), widget.height())
