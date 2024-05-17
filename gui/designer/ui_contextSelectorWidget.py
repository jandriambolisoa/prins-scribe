# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contextSelectorWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_contextSelectorWidget(object):
    def setupUi(self, contextSelectorWidget):
        if not contextSelectorWidget.objectName():
            contextSelectorWidget.setObjectName(u"contextSelectorWidget")
        contextSelectorWidget.resize(432, 354)
        self.verticalLayout = QVBoxLayout(contextSelectorWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.contextContainer = QHBoxLayout()
        self.contextContainer.setObjectName(u"contextContainer")
        self.contextLabel = QLabel(contextSelectorWidget)
        self.contextLabel.setObjectName(u"contextLabel")

        self.contextContainer.addWidget(self.contextLabel)

        self.projectLineEdit = QLineEdit(contextSelectorWidget)
        self.projectLineEdit.setObjectName(u"projectLineEdit")
        self.projectLineEdit.setEnabled(False)

        self.contextContainer.addWidget(self.projectLineEdit)

        self.dccLineEdit = QLineEdit(contextSelectorWidget)
        self.dccLineEdit.setObjectName(u"dccLineEdit")
        self.dccLineEdit.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dccLineEdit.sizePolicy().hasHeightForWidth())
        self.dccLineEdit.setSizePolicy(sizePolicy)

        self.contextContainer.addWidget(self.dccLineEdit)

        self.horizontalSpacer = QSpacerItem(60, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.contextContainer.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.contextContainer)

        self.itemContainer = QHBoxLayout()
        self.itemContainer.setObjectName(u"itemContainer")
        self.showLabel = QLabel(contextSelectorWidget)
        self.showLabel.setObjectName(u"showLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.showLabel.sizePolicy().hasHeightForWidth())
        self.showLabel.setSizePolicy(sizePolicy1)

        self.itemContainer.addWidget(self.showLabel)

        self.showsComboBox = QComboBox(contextSelectorWidget)
        self.showsComboBox.setObjectName(u"showsComboBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.showsComboBox.sizePolicy().hasHeightForWidth())
        self.showsComboBox.setSizePolicy(sizePolicy2)

        self.itemContainer.addWidget(self.showsComboBox)

        self.horizontalSpacer_3 = QSpacerItem(60, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.itemContainer.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.itemContainer)

        self.line = QFrame(contextSelectorWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.listFiltersContainer = QHBoxLayout()
        self.listFiltersContainer.setObjectName(u"listFiltersContainer")
        self.assetsRadioBtn = QRadioButton(contextSelectorWidget)
        self.assetsRadioBtn.setObjectName(u"assetsRadioBtn")
        self.assetsRadioBtn.setChecked(True)

        self.listFiltersContainer.addWidget(self.assetsRadioBtn)

        self.shotsRadioBtn = QRadioButton(contextSelectorWidget)
        self.shotsRadioBtn.setObjectName(u"shotsRadioBtn")

        self.listFiltersContainer.addWidget(self.shotsRadioBtn)

        self.taskLabel = QLabel(contextSelectorWidget)
        self.taskLabel.setObjectName(u"taskLabel")
        sizePolicy1.setHeightForWidth(self.taskLabel.sizePolicy().hasHeightForWidth())
        self.taskLabel.setSizePolicy(sizePolicy1)

        self.listFiltersContainer.addWidget(self.taskLabel)

        self.taskComboBox = QComboBox(contextSelectorWidget)
        self.taskComboBox.setObjectName(u"taskComboBox")
        sizePolicy2.setHeightForWidth(self.taskComboBox.sizePolicy().hasHeightForWidth())
        self.taskComboBox.setSizePolicy(sizePolicy2)

        self.listFiltersContainer.addWidget(self.taskComboBox)

        self.horizontalSpacer_2 = QSpacerItem(60, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.listFiltersContainer.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.listFiltersContainer)

        self.listContainer = QHBoxLayout()
        self.listContainer.setObjectName(u"listContainer")
        self.listWidget = QListWidget(contextSelectorWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.listContainer.addWidget(self.listWidget)

        self.listActionsContainer = QVBoxLayout()
        self.listActionsContainer.setObjectName(u"listActionsContainer")
        self.addBtn = QPushButton(contextSelectorWidget)
        self.addBtn.setObjectName(u"addBtn")

        self.listActionsContainer.addWidget(self.addBtn)

        self.variationBtn = QPushButton(contextSelectorWidget)
        self.variationBtn.setObjectName(u"variationBtn")
        self.variationBtn.setEnabled(False)

        self.listActionsContainer.addWidget(self.variationBtn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.listActionsContainer.addItem(self.verticalSpacer)


        self.listContainer.addLayout(self.listActionsContainer)


        self.verticalLayout.addLayout(self.listContainer)


        self.retranslateUi(contextSelectorWidget)

        QMetaObject.connectSlotsByName(contextSelectorWidget)
    # setupUi

    def retranslateUi(self, contextSelectorWidget):
        contextSelectorWidget.setWindowTitle(QCoreApplication.translate("contextSelectorWidget", u"Form", None))
        self.contextLabel.setText(QCoreApplication.translate("contextSelectorWidget", u"Context :", None))
        self.showLabel.setText(QCoreApplication.translate("contextSelectorWidget", u"Show :", None))
        self.assetsRadioBtn.setText(QCoreApplication.translate("contextSelectorWidget", u"Assets", None))
        self.shotsRadioBtn.setText(QCoreApplication.translate("contextSelectorWidget", u"Shots", None))
        self.taskLabel.setText(QCoreApplication.translate("contextSelectorWidget", u"Task :", None))
        self.addBtn.setText(QCoreApplication.translate("contextSelectorWidget", u"Add", None))
        self.variationBtn.setText(QCoreApplication.translate("contextSelectorWidget", u"Create\n"
"variation", None))
    # retranslateUi

