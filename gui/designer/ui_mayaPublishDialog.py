# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mayaPublishDialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_mayaPublishDialogWidget(object):
    def setupUi(self, mayaPublishDialogWidget):
        if not mayaPublishDialogWidget.objectName():
            mayaPublishDialogWidget.setObjectName(u"mayaPublishDialogWidget")
        mayaPublishDialogWidget.resize(313, 213)
        self.verticalLayout = QVBoxLayout(mayaPublishDialogWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.assetBtnContainer = QVBoxLayout()
        self.assetBtnContainer.setObjectName(u"assetBtnContainer")
        self.mayaAssetBtn = QCheckBox(mayaPublishDialogWidget)
        self.mayaAssetBtn.setObjectName(u"mayaAssetBtn")

        self.assetBtnContainer.addWidget(self.mayaAssetBtn)

        self.assetFbxBtn = QCheckBox(mayaPublishDialogWidget)
        self.assetFbxBtn.setObjectName(u"assetFbxBtn")

        self.assetBtnContainer.addWidget(self.assetFbxBtn)

        self.assetAbcBtn = QCheckBox(mayaPublishDialogWidget)
        self.assetAbcBtn.setObjectName(u"assetAbcBtn")

        self.assetBtnContainer.addWidget(self.assetAbcBtn)


        self.verticalLayout.addLayout(self.assetBtnContainer)

        self.line = QFrame(mayaPublishDialogWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.shotBtnContainer = QVBoxLayout()
        self.shotBtnContainer.setObjectName(u"shotBtnContainer")
        self.mayaShotBtn = QCheckBox(mayaPublishDialogWidget)
        self.mayaShotBtn.setObjectName(u"mayaShotBtn")

        self.shotBtnContainer.addWidget(self.mayaShotBtn)

        self.animFbxBtn = QCheckBox(mayaPublishDialogWidget)
        self.animFbxBtn.setObjectName(u"animFbxBtn")

        self.shotBtnContainer.addWidget(self.animFbxBtn)

        self.animAbcBtn = QCheckBox(mayaPublishDialogWidget)
        self.animAbcBtn.setObjectName(u"animAbcBtn")

        self.shotBtnContainer.addWidget(self.animAbcBtn)


        self.verticalLayout.addLayout(self.shotBtnContainer)


        self.retranslateUi(mayaPublishDialogWidget)

        QMetaObject.connectSlotsByName(mayaPublishDialogWidget)
    # setupUi

    def retranslateUi(self, mayaPublishDialogWidget):
        mayaPublishDialogWidget.setWindowTitle(QCoreApplication.translate("mayaPublishDialogWidget", u"Form", None))
        self.mayaAssetBtn.setText(QCoreApplication.translate("mayaPublishDialogWidget", u"mayaAsset (.ma)", None))
        self.assetFbxBtn.setText(QCoreApplication.translate("mayaPublishDialogWidget", u"assetFbx (.fbx)", None))
        self.assetAbcBtn.setText(QCoreApplication.translate("mayaPublishDialogWidget", u"assetAlembic (.abc)", None))
        self.mayaShotBtn.setText(QCoreApplication.translate("mayaPublishDialogWidget", u"mayaShot (.ma)", None))
        self.animFbxBtn.setText(QCoreApplication.translate("mayaPublishDialogWidget", u"animFbx (.fbx)", None))
        self.animAbcBtn.setText(QCoreApplication.translate("mayaPublishDialogWidget", u"animAlembic (.abc)", None))
    # retranslateUi

