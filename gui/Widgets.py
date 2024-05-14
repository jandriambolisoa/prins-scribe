from prins              import __PROJECTPATH__
from prins.api          import Asset
from prins.api          import Show
from prins.api          import Episode
from prins.api          import Sequence
from prins.api          import Shot
from prins.api          import Task
from prins.api          import Category
from prinspyqt.Graphics import getPrinsStyleSheet, getStyleSheet

from PySide2            import QtWidgets
from PySide2            import QtGui

from designer.ui_contextSelectorWidget  import Ui_contextSelectorWidget
from designer.ui_mayaScribeWidget       import Ui_mayaScribeWidget
from designer.ui_mayaPublishDialog      import Ui_mayaPublishDialogWidget

class ContextSelector(Ui_contextSelectorWidget, QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.listDatas = []


    def setContext(self, projectRoot, dcc):
        """Sets the context displayed

        :param projectPath: The current project path
        :type projectPath: str
        :param dcc: The DCC running this app
        :type dcc: str
        """

        self.projectLineEdit.setText(projectRoot)
        self.dccLineEdit.setText(dcc)


    def updateShowComboBox(self):
        """Add available shows in the show combo box
        """

        ##TODO Take in account the current user.shows property
        projectRoot = self.projectLineEdit.text()
        allShows = Show.search(projectRoot, "*")

        self.showsComboBox.clear()
        self.showsComboBox.addItems(allShows)
        

    def updateTaskComboBox(self):
        """Updates the task combo box
        """

        # Get tasks as int
        assetTasks = [t for t in Task._listValues() if t < 50 or t == 99]
        shotTasks = [t for t in Task._listValues() if t > 50]

        # Clear task combo box
        self.taskComboBox.clear()

        # Get radio buttons state and populate
        if self.assetsRadioBtn.isChecked():
            for task in assetTasks:
                self.taskComboBox.addItem(text = Task().asString(task))

        elif self.shotsRadioBtn.isChecked():
            for task in shotTasks:
                self.taskComboBox.addItem(text = Task().asString(task))


    def updateListView(self):
        """Update the list view
        """

        # Reset list datas
        self.listDatas = []

        projectRoot = self.projectLineEdit.text()
        show = self.showsComboBox.currentText()

        # Asset
        if self.assetsRadioBtn.isChecked():
            allAssets = Asset.search(projectRoot, show, searchBy="showId")
            for a in allAssets:
                
                # Get each asset
                asset = Asset.get(projectRoot, a)
                assetDatas = {
                    "display": "%s | %s"%(asset.id, asset.description),
                    "Asset": asset.id
                }

                # Add them in list datas
                self.listDatas.append(assetDatas)
                
                for var in asset.variations:
                    if var:
                        assetDatas = {
                            "display": "%s%s | %s variation"%(asset.id, var, asset.id),
                            "Asset": "%s%s"%(asset.id, var)
                        }

                        # Add their variations
                        self.listDatas.append(assetDatas)

        # Shot
        elif self.shotsRadioBtn.isChecked():

            allEpisodes = Episode.search(projectRoot, show, "*")

            for episode in allEpisodes:
                sequences = Sequence.search(projectRoot, show, episode, "*")

                for seq in sequences:
                    shots = Shot.search(projectRoot, show, episode, seq, "*")

                    for s in shots:
                        shotDatas = {
                            "display": "%s | %s | %s"%(episode, seq, s),
                            "Episode": episode,
                            "Sequence": seq,
                            "Shot": s
                        }

                        self.listDatas.append(shotDatas)

        # Update List Widget
        self.listWidget.clear()
        itemsToAdd = [item["display"] for item in self.listDatas]
        self.listWidget.addItems(itemsToAdd)


    def createAsset(self):
        """Creates an asset with user inputs.
        """

        name, ok = QtWidgets.QInputDialog.getText(
            self,
            "Create asset",
            "Asset id:",
            QtWidgets.QLineEdit.Normal
        )

        if not ok:
            return

        # Get Asset categories
        assetCategories = [c for c in Category._listValues() if c < 50]
        allCategories = []
        for cat in assetCategories:
            allCategories.append(text = Category().asString(cat))

        category, ok = QtWidgets.QInputDialog.getItem(
            self,
            "What is this asset category ?",
            "Category:",
            allCategories,
            0,
            False
        )

        if not ok:
            return
        
        description, ok = QtWidgets.QInputDialog.getText(
            self,
            "Describe this asset (optional)",
            "Description:",
            QtWidgets.QLineEdit.Normal
        )

        if not ok:
            description = "No description."

        if name and category and description:
            Asset.create(
                self.projectLineEdit.text(),
                category=[category],
                showId=[self.showsComboBox.currentText()],
                description=description
            )

            self.updateListView()


    def createVariation(self):

        selection = self.listWidget.selectedIndexes()
        selectionData = self.listDatas[selection[0]]

        variationName, ok = QtWidgets.QInputDialog.getText(
            self,
            "%s variation name."%(selectionData["Asset"]),
            "%s variation:"%(selectionData["Asset"]),
            QtWidgets.QLineEdit.Normal
        )

        if ok and variationName:

            asset = Asset.get(
                self.projectLineEdit.text(),
                selectionData["Asset"]
            )
        
            assetVars = asset.variations
            assetVars.append(variationName)

            asset.modify(assetVars, "variations")

            self.updateListView()

    
    def updateVariationBtnStatus(self):
        """Update variationBtn status
        """

        if self.assetsRadioBtn.isChecked():
            selection = self.listWidget.selectedIndexes()
            selectionData = self.listDatas[selection[0]]
            name = selectionData["Asset"]

            if name in Asset.search(self.projectLineEdit.text(), name, perfectMatch = True):
                self.variationBtn.setEnabled()
            else:
                self.variationBtn.setDisabled()

        elif self.shotsRadioBtn.isChecked():
            self.variationBtn.setDisabled()


    def updateAddBtnStatus(self):
        """Update addBtn status
        """

        if self.assetsRadioBtn.isChecked():
            self.addBtn.setEnabled()
        elif self.shotsRadioBtn.isChecked():
            self.variationBtn.setDisabled()


class MayaScribeWidget(Ui_mayaScribeWidget, QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

class MayaScribePublishDialog(Ui_mayaPublishDialogWidget, QtWidgets.QWidget):

    def __init__(self, mode):
        super().__init__()
        self.setupUi(self)

        if mode == "Asset":
            for btn in self.shotBtnContainer.children():
                btn.setDisabled()

        elif mode == "Shot":
            for btn in self.assetBtnContainer.children():
                btn.setDisabled()