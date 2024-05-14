from prins import __PROJECTPATH__
from prinspyqt.Graphics import getPrinsStyleSheet
from prinspyqt.Graphics import getIcon

from PySide2            import QtWidgets
from PySide2            import QtGui
from PySide2            import QtCore

from .widgets    import ContextSelector
from .widgets    import MayaScribeWidget, MayaScribePublishDialog

class ScribeWindow(QtWidgets.QMainWindow):

    window = None

    def __init__(self, dcc, parent = None):
        super().__init__(parent=parent)

        # Sanity check
        if not isinstance(dcc, str):
            raise TypeError("DCC not recognized")

        # Setup window
        self.setObjectName("Scribe")
        self.setWindowTitle("PRINS Scribe 0.0.1")
        self.setWindowIcon(getIcon(__file__, "scribeWindow"))
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        self.setStyleSheet(getPrinsStyleSheet())
        self.fullWidget = QtWidgets.QWidget()
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setSpacing(0)
        self.mainLayout.setContentsMargins(0,0,0,0)
        self.fullWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.fullWidget)

        # Setup widgets
        self.commonWidget = ContextSelector()
        self.commonWidget.setContext(__PROJECTPATH__, dcc)
        self.commonWidget.updateShowComboBox()
        self.commonWidget.updateTaskComboBox()
        self.commonWidget.updateListView()
        self.mainLayout.addWidget(self.commonWidget)

        if dcc == "MAYA":
            self.actionWidget = MayaScribeWidget()
            self.mainLayout.addWidget(self.actionWidget)

        # Interactivity
        self.commonWidget.showsComboBox.currentTextChanged.connect(self.commonWidget.updateListView)
        self.commonWidget.shotsRadioBtn.clicked.connect(self.commonWidget.updateTaskComboBox)
        self.commonWidget.assetsRadioBtn.clicked.connect(self.commonWidget.updateTaskComboBox)
        self.commonWidget.shotsRadioBtn.clicked.connect(self.commonWidget.updateAddBtnStatus)
        self.commonWidget.assetsRadioBtn.clicked.connect(self.commonWidget.updateAddBtnStatus)
        self.commonWidget.addBtn.clicked.connect(self.commonWidget.createAsset)
        self.commonWidget.variationBtn.clicked.connect(self.commonWidget.createVariation)


class ScribeMayaPublishDialogWindow(QtWidgets.QDialog):

    window = None

    def __init__(self, mode, parent = None):
        super().__init__(parent=parent)

        self.formats = []

        # Setup window
        self.setObjectName("ScribeMayaPublishDialog")
        self.setWindowTitle("Select publish formats...")
        self.setWindowIcon(getIcon(__file__, "scribeWindow"))
        self.setStyleSheet(getPrinsStyleSheet())
        self.fullWidget = QtWidgets.QWidget()
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setSpacing(0)
        self.mainLayout.setContentsMargins(0,0,0,0)
        self.fullWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.fullWidget)

        # Setup dialog buttons
        buttons = QtWidgets.QDialogButtonBox.Ok
        self.buttonBox = QtWidgets.QDialogButtonBox(buttons)
        self.buttonBox.accepted.connect(self.getSelectedFormats)

        # Setup widgets
        self.mainWidget = MayaScribePublishDialog(mode)
        self.mainLayout.addWidget(self.commonWidget)
        self.mainLayout.addWidget(self.buttonBox)


    def getSelectedFormats(self):

        self.formats = []

        for btn in self.mainWidget.assetBtnContainer.children():
            if btn.isChecked():
                self.formats.append(btn.objectName())

        for btn in self.mainWidget.shotBtnContainer.children():
            if btn.isChecked():
                self.formats.append(btn.objectName())

        return self.formats
