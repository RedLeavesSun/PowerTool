#!/usr/bin/python3
# -*- coding=utf-8 -*-
# author:   RedLeaves
# date:     2022/02/25
# version:  1.0


import PySide6
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtCore import (Slot, Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtGui import (QPaintEvent, QPen)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QWidget)


class Demo(QWidget):
    def paintEvent(self, event: QPaintEvent) -> None:
        # return super().paintEvent(event)

        painter = QPainter(self)
        pen = QPen()

        pen.setColor(Qt.green)
        pen.setStyle(Qt.SolidLine)
        pen.setWidthF(0.05)

        painter.setPen(pen)
        painter.setViewport(50, 50, self.width()-100, self.height()-100)
        painter.setWindow(-10, 2, 20, -4)
        painter.fillRect(-10, 2, 20, -4, Qt.white)
        # painter.drawLine(Qt.QPointF(-10, 0), Qt.QPointF(10, 0))
        # painter.drawLine(Qt.QPointF(0, 2), Qt.QPointF(0, -2))

        painter.end()

