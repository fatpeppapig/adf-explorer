from PyQt5.QtWidgets import QAction, qApp
from PyQt5.QtGui import QIcon


class Actions():
    def __init__(self, app):
        self.createAction = QAction(QIcon('icons/floppy.png'), 'Create', app)
        self.createAction.setShortcut('Ctrl+N')
        self.createAction.triggered.connect(app.createAdf)

        self.openAction = QAction(QIcon('icons/hdd.png'), 'Open', app)
        self.openAction.setShortcut('Ctrl+O')
        self.openAction.triggered.connect(app.openAdf)

        self.parentAction = QAction(QIcon('icons/return.png'), 'Parent', app)
        self.parentAction.setShortcut('Backspace')
        self.parentAction.triggered.connect(app.parent)

        self.makeDirAction = QAction(
            QIcon('icons/add-folder.png'), 'Make Directory', app)
        self.makeDirAction.setShortcut('Ctrl+Shift+N')
        self.makeDirAction.triggered.connect(app.makeDir)

        self.extractAction = QAction(
            QIcon('icons/download.png'), 'Extract', app)
        self.extractAction.setShortcut('Ctrl+D')
        self.extractAction.triggered.connect(app.extract)

        self.insertAction = QAction(QIcon('icons/upload.png'), 'Insert', app)
        self.insertAction.setShortcut('Ctrl+I')
        self.insertAction.triggered.connect(app.insert)

        self.deleteAction = QAction(QIcon('icons/remove.png'), 'Delete', app)
        self.deleteAction.setShortcut('Delete')
        self.deleteAction.triggered.connect(app.delete)

        self.quitAction = QAction(QIcon('icons/exit.png'), 'Quit', app)
        self.quitAction.setShortcut('Ctrl+Q')
        self.quitAction.triggered.connect(qApp.quit)

        self.disableAdfActions()

    def disableAdfActions(self):
        self.parentAction.setDisabled(True)
        self.makeDirAction.setDisabled(True)
        self.extractAction.setDisabled(True)
        self.insertAction.setDisabled(True)
        self.deleteAction.setDisabled(True)

    def enableAdfActions(self):
        self.parentAction.setDisabled(False)
        self.makeDirAction.setDisabled(False)
        self.insertAction.setDisabled(False)

    def disableFileActions(self):
        self.extractAction.setDisabled(True)
        self.deleteAction.setDisabled(True)

    def enableFileActions(self):
        self.extractAction.setDisabled(False)
        self.deleteAction.setDisabled(False)
