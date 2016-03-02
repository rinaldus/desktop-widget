# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DesktopWidget(object):
    def setupUi(self, DesktopWidget):
        DesktopWidget.setObjectName("DesktopWidget")
        DesktopWidget.resize(670, 481)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DesktopWidget.sizePolicy().hasHeightForWidth())
        DesktopWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QtWidgets.QHBoxLayout(DesktopWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.retranslateUi(DesktopWidget)
        QtCore.QMetaObject.connectSlotsByName(DesktopWidget)

    def retranslateUi(self, DesktopWidget):
        _translate = QtCore.QCoreApplication.translate
        DesktopWidget.setWindowTitle(_translate("DesktopWidget", "Desktop Widget"))

import resources_rc
