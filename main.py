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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QWidget)

from context import Context

from window.MainWindow import MainWindow
from window.SelectDeviceWindow import SelectDeviceWindow
from window.ReflashWindow import ReflashWindow
from window.SetVoutWindow import SetVoutWindow
from window.ParametersWindow import ParametersWindow
from window.TriggerSettingsWindow import TriggerSettingsWindow

import Monsoon.HVPM as HVPM
import Monsoon.LVPM as LVPM


def main():
    app = QApplication([])

    context = Context()

    monsoon = HVPM.Monsoon()

    mainWindow = MainWindow(context)
    selectDeviceWindow = SelectDeviceWindow(context)
    reflashWindow = ReflashWindow(context)
    setVoutWindow = SetVoutWindow(context)
    parametersWindow = ParametersWindow(context)
    triggerSettingsWindow = TriggerSettingsWindow(context)

    selectDeviceWindow.setMainWindow(mainWindow)
    selectDeviceWindow.setReflashWindow(reflashWindow)

    mainWindow.setSetVoutWindow(setVoutWindow)
    mainWindow.setParametersWindow(parametersWindow)
    mainWindow.setTriggerSettingsWindow(triggerSettingsWindow)

    mainWindow.setMonsoon(monsoon)
    selectDeviceWindow.setMonsoon(monsoon)
    reflashWindow.setMonsoon(monsoon)
    setVoutWindow.setMonsoon(monsoon)
    parametersWindow.setMonsoon(monsoon)
    triggerSettingsWindow.setMonsoon(monsoon)

    selectDeviceWindow.show()

    app.exec()


if __name__ == "__main__":
    main()
