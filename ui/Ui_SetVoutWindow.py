# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SetVoutWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_SetVoutWindow(object):
    def setupUi(self, SetVoutWindow):
        if not SetVoutWindow.objectName():
            SetVoutWindow.setObjectName(u"SetVoutWindow")
        SetVoutWindow.resize(216, 320)
        self.centralwidget = QWidget(SetVoutWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(8, 8, 201, 271))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.rbTypical = QRadioButton(self.verticalLayoutWidget)
        self.rbTypical.setObjectName(u"rbTypical")
        self.rbTypical.setChecked(True)

        self.verticalLayout.addWidget(self.rbTypical)

        self.rbLow = QRadioButton(self.verticalLayoutWidget)
        self.rbLow.setObjectName(u"rbLow")

        self.verticalLayout.addWidget(self.rbLow)

        self.rbHigh = QRadioButton(self.verticalLayoutWidget)
        self.rbHigh.setObjectName(u"rbHigh")

        self.verticalLayout.addWidget(self.rbHigh)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.rbDigtal = QRadioButton(self.verticalLayoutWidget)
        self.rbDigtal.setObjectName(u"rbDigtal")
        self.rbDigtal.setStyleSheet(u"")
        self.rbDigtal.setChecked(False)
        self.rbDigtal.setAutoRepeat(False)

        self.verticalLayout.addWidget(self.rbDigtal)

        self.rbThreeCell = QRadioButton(self.verticalLayoutWidget)
        self.rbThreeCell.setObjectName(u"rbThreeCell")

        self.verticalLayout.addWidget(self.rbThreeCell)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.rbCustom = QRadioButton(self.verticalLayoutWidget)
        self.rbCustom.setObjectName(u"rbCustom")

        self.horizontalLayout.addWidget(self.rbCustom)

        self.edCustom = QLineEdit(self.verticalLayoutWidget)
        self.edCustom.setObjectName(u"edCustom")

        self.horizontalLayout.addWidget(self.edCustom)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.btnOk = QPushButton(self.centralwidget)
        self.btnOk.setObjectName(u"btnOk")
        self.btnOk.setGeometry(QRect(8, 288, 89, 25))
        self.btnCancel = QPushButton(self.centralwidget)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setGeometry(QRect(120, 288, 89, 25))
        SetVoutWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SetVoutWindow)

        QMetaObject.connectSlotsByName(SetVoutWindow)
    # setupUi

    def retranslateUi(self, SetVoutWindow):
        SetVoutWindow.setWindowTitle(QCoreApplication.translate("SetVoutWindow", u"Set Vout", None))
        self.label.setText(QCoreApplication.translate("SetVoutWindow", u"Cell Phone", None))
        self.rbTypical.setText(QCoreApplication.translate("SetVoutWindow", u"Typical(3.70V)", None))
        self.rbLow.setText(QCoreApplication.translate("SetVoutWindow", u"Low(3.35V)", None))
        self.rbHigh.setText(QCoreApplication.translate("SetVoutWindow", u"High(4.2V)", None))
        self.label_2.setText(QCoreApplication.translate("SetVoutWindow", u"High Voltage: 5-13.5V", None))
        self.rbDigtal.setText(QCoreApplication.translate("SetVoutWindow", u"Digtal(5V)", None))
        self.rbThreeCell.setText(QCoreApplication.translate("SetVoutWindow", u"3-cell(11.1V)", None))
        self.rbCustom.setText(QCoreApplication.translate("SetVoutWindow", u"Custom", None))
        self.btnOk.setText(QCoreApplication.translate("SetVoutWindow", u"OK", None))
        self.btnCancel.setText(QCoreApplication.translate("SetVoutWindow", u"Cancel", None))
    # retranslateUi

