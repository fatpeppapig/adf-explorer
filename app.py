from PyQt5.QtWidgets import QMainWindow, QFileDialog, QInputDialog, QMessageBox

from adf import ADF

from actions import Actions
from toolbar import Toolbar
from menu import Menu
from path import Path
from status import Status
from browser import Browser


class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = 'ADF Explorer'
        self.width = 640
        self.height = 512

        self.adf = ADF(self)

        self.actions = Actions(self)
        self.toolbar = Toolbar(self)
        self.menu = Menu(self)
        self.path = Path(self)
        self.browser = Browser(self)
        self.status = Status(self)

        self.initUI()

    def updateStatusBarMessage(self):
        self.status.setText()

    def updateWindowTitle(self):
        if self.adf.volume:
            self.setWindowTitle(self.title + ': ' +
                                self.adf.volumeName())
        else:
            self.setWindowTitle(self.title)

    def updatePath(self, path):
        self.path.setText(path)

    def updateBrowser(self, entries):
        self.browser.populate(entries)

    def parent(self):
        self.adf.parent()
        self.browser.deselect()

    def navigate(self, path):
        self.adf.navigate(path)
        self.browser.deselect()

    def navigateDown(self, dir):
        self.adf.navigateDown(dir)
        self.browser.deselect()

    def enableFileActions(self):
        self.actions.enableFileActions()

    def disableFileActions(self):
        self.actions.disableFileActions()

    def makeDir(self):
        name, ok = QInputDialog.getText(
            self, 'Make Directory', 'Please enter a new directory name:')

        if name and ok:
            self.adf.makeDir(name)

    def relabel(self):
        name, ok = QInputDialog.getText(
            self, 'Relabel', 'Please enter a new volume name:')

        if name and ok:
            self.adf.relabel(name)
            self.updateWindowTitle()

    def delete(self):
        msgbox = QMessageBox(QMessageBox.Question, 'Confirm delete',
                             'Are you sure you want to delete %s' % self.browser.selectedItem())
        msgbox.addButton(QMessageBox.Yes)
        msgbox.addButton(QMessageBox.No)

        result = msgbox.exec()
        if result == QMessageBox.Yes:
            self.adf.delete(self.browser.selectedItem())

    def extract(self):
        path, _ = QFileDialog.getSaveFileName(
            self, 'QFileDialog.getSaveFileName()', '', '', options=QFileDialog.Options())

        if path:
            self.adf.extract(self.browser.selectedItem(), path)

    def insert(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile & QFileDialog.Directory)

        if dialog.exec_():
            paths = dialog.selectedFiles()

            for path in paths:
                self.adf.insert(path)

    def createAdf(self):
        path, _ = QFileDialog.getSaveFileName(
            self, 'QFileDialog.getSaveFileName()', '', '', options=QFileDialog.Options())

        if path:
            self.adf.create(path)
            self.startBrowsing()

    def openAdf(self):
        path, _ = QFileDialog.getOpenFileName(
            self, 'QFileDialog.getOpenFileName()', '', 'ADF Files (*.adf)', options=QFileDialog.Options())

        if path:
            self.adf.open(path)
            self.startBrowsing()

    def startBrowsing(self, path='/'):
        self.actions.enableAdfActions()
        self.status.setText(self.adf.volumeInfo())
        self.path.enable()
        self.updateWindowTitle()
        self.navigate(path)

    def initUI(self):
        self.setFixedSize(self.width, self.height)
        self.updateWindowTitle()

        self.show()

    def cleanUp(self):
        self.adf.cleanUp()
