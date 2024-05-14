# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mayaScribeWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_mayaScribeWidget(object):
    def setupUi(self, mayaScribeWidget):
        if not mayaScribeWidget.objectName():
            mayaScribeWidget.setObjectName(u"mayaScribeWidget")
        mayaScribeWidget.resize(574, 44)
        self.verticalLayout = QVBoxLayout(mayaScribeWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.actionsContainer = QHBoxLayout()
        self.actionsContainer.setObjectName(u"actionsContainer")
        self.saveBtn = QPushButton(mayaScribeWidget)
        self.saveBtn.setObjectName(u"saveBtn")

        self.actionsContainer.addWidget(self.saveBtn)

        self.deliverBtn = QPushButton(mayaScribeWidget)
        self.deliverBtn.setObjectName(u"deliverBtn")

        self.actionsContainer.addWidget(self.deliverBtn)

        self.publishBtn = QPushButton(mayaScribeWidget)
        self.publishBtn.setObjectName(u"publishBtn")

        self.actionsContainer.addWidget(self.publishBtn)


        self.verticalLayout.addLayout(self.actionsContainer)


        self.retranslateUi(mayaScribeWidget)

        QMetaObject.connectSlotsByName(mayaScribeWidget)
    # setupUi

    def retranslateUi(self, mayaScribeWidget):
        mayaScribeWidget.setWindowTitle(QCoreApplication.translate("mayaScribeWidget", u"Form", None))
        self.saveBtn.setText(QCoreApplication.translate("mayaScribeWidget", u"Save file", None))
        self.deliverBtn.setText(QCoreApplication.translate("mayaScribeWidget", u"Blast and Deliver", None))
        self.publishBtn.setText(QCoreApplication.translate("mayaScribeWidget", u"Publish selection", None))
    # retranslateUi

