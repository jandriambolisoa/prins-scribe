from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets

from shiboken2  import wrapInstance

from prins.api import Asset
from prins.api import Shot

from maya import cmds

from gui.windows import ScribeWindow
from gui.windows import ScribeMayaPublishDialogWindow

from core import maya as m

import os

class ScribeApp(ScribeWindow):

    def __init__(self, dcc, parent=None):
        super().__init__(dcc, parent)

        if dcc == "MAYA":
            self.actionWidget.saveBtn.clicked.connect(self.saveAction)
            self.actionWidget.deliverBtn.clicked.connect(self.deliverAction)
            self.actionWidget.publishBtn.clicked.connect(self.publishAction)

            self.setObjectName("ScribeApp")

    def saveAction(self):
        """Saves the selected item.
        """
        
        projectRoot = self.commonWidget.projectLineEdit.text()
        selectionIndex = self.commonWidget.listWidget.selectedIndexes()[0].row()

        task = self.commonWidget.taskComboBox.currentText()
        dcc = self.commonWidget.dccLineEdit.text()

        if self.commonWidget.assetsRadioBtn.isChecked():

            asset = self.commonWidget.listDatas[selectionIndex]["Asset"]
            m.saveAsset(
                projectRoot,
                asset,
                task,
                dcc
            )

        elif self.commonWidget.shotsRadioBtn.isChecked():

            show = self.commonWidget.showsComboBox.currentText()
            episode = self.commonWidget.listDatas[selectionIndex]["Episode"]
            sequence = self.commonWidget.listDatas[selectionIndex]["Sequence"]
            shot = self.commonWidget.listDatas[selectionIndex]["Shot"]

            m.saveShot(
                projectRoot,
                show,
                episode,
                sequence,
                shot,
                task,
                dcc
            )

    
    def deliverAction(self):
        """Creates a blast and delivers the selected item
        """

        projectRoot = self.commonWidget.projectLineEdit.text()
        selectionIndex = self.commonWidget.listWidget.selectedIndexes()[0].row()   
        task = self.commonWidget.taskComboBox.currentText()
        dcc = self.commonWidget.dccLineEdit.text()

        saveName = cmds.file(query = True, sceneName = True, shortName = True)
        notSaved = cmds.file(query = True, modified = True)

        if notSaved:
            raise Exception("Scene have unsaved changes.")

        version = os.path.splitext(saveName)[0].split("_")[-1]
        size = [1920,1080] #TODO Allow user to use different sizes

        if self.commonWidget.assetsRadioBtn.isChecked():

            fileTemplate = "movAsset" #TODO Allow user to choose different
            asset = self.commonWidget.listDatas[selectionIndex]["Asset"]

            m.deliverAsset(
                projectRoot,
                asset,
                task,
                version,
                fileTemplate,
                size
            )

        elif self.commonWidget.shotsRadioBtn.isChecked():

            fileTemplate = "movShot" #TODO Allow user to choose different
            show = self.commonWidget.showsComboBox.currentText()
            episode = self.commonWidget.listDatas[selectionIndex]["Episode"]
            sequence = self.commonWidget.listDatas[selectionIndex]["Sequence"]
            shot = self.commonWidget.listDatas[selectionIndex]["Shot"]

            m.deliverShot(
                projectRoot,
                show,
                episode,
                sequence,
                shot,
                task,
                version,
                fileTemplate,
                size
            )


    def publishAction(self):

        projectRoot = self.commonWidget.projectLineEdit.text()
        selectionIndex = self.commonWidget.listWidget.selectedIndexes()[0].row()    
        task = self.commonWidget.taskComboBox.currentText()
        dcc = self.commonWidget.dccLineEdit.text()

        saveName = cmds.file(query = True, sceneName = True, shortName = True)
        notSaved = cmds.file(query = True, modified = True)

        if notSaved:
            raise Exception("Scene have unsaved changes.")

        version = os.path.splitext(saveName)[0].split("_")[-1]
        
        if self.commonWidget.assetsRadioBtn.isChecked() and self.commonWidget.dccLineEdit.text() == "MAYA":

            asset = self.commonWidget.listDatas[selectionIndex]["Asset"]

            mayaPublishDialog = ScribeMayaPublishDialogWindow("Asset")
            if mayaPublishDialog.exec_() == QtWidgets.QDialog.Accepted:
                fileTemplates = mayaPublishDialog.getSelectedFormats()

                for ft in fileTemplates:

                    m.publishAsset(
                        projectRoot,
                        asset,
                        task,
                        version,
                        self._normFileTemplate(ft)
                    )

        if self.commonWidget.shotsRadioBtn.isChecked() and self.commonWidget.dccLineEdit.text() == "MAYA":

            show = self.commonWidget.showsComboBox.currentText()
            episode = self.commonWidget.listDatas[selectionIndex]["Episode"]
            sequence = self.commonWidget.listDatas[selectionIndex]["Sequence"]
            shot = self.commonWidget.listDatas[selectionIndex]["Shot"]

            mayaPublishDialog = ScribeMayaPublishDialogWindow("Shot")
            if mayaPublishDialog.exec_() == QtWidgets.QDialog.Accepted:
                fileTemplates = mayaPublishDialog.getSelectedFormats()
                mayaPublishDialog.hide()

            for ft in fileTemplates:

                m.publishShot(
                    projectRoot,
                    show,
                    episode,
                    sequence,
                    shot,
                    task,
                    version,
                    self._normFileTemplate(ft)
                )


    def _normFileTemplate(self, btnName):

        fileTemplatesBtn = {
            "mayaAssetBtn": "mayaAsset",
            "assetFbxBtn": "assetFbx",
            "assetAbcBtn": "assetAlembic",
            "mayaShotBtn": "mayaShot",
            "animFbxBtn": "animFbx",
            "animAbcBtn": "animAlembic"
        }

        return fileTemplatesBtn[btnName]

def openApp():
    from maya import OpenMayaUI
    import sys

    if QtWidgets.QApplication.instance():
        for win in (QtWidgets.QApplication.allWindows()):
            if 'ScribeApp' in win.objectName(): # update this name to match name below
                win.destroy()

    ptr = OpenMayaUI.MQtUtil.mainWindow()
    mayaMainWindow = wrapInstance(int(ptr), QtWidgets.QWidget)

    # Get app name
    if "maya.exe" in sys.argv[0]:
        appName = "MAYA"

    if not ScribeApp.window:
        ScribeApp.window = ScribeApp(dcc= appName, parent= mayaMainWindow)

    ScribeApp.window.show()
