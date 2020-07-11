from PyQt5.QtWidgets import QAction, qApp
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore


class Toolbar():
    def __init__(self, app):
        self.toolbar = app.addToolBar('Toolbar')
        self.toolbar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.toolbar.addAction(app.actions.createAction)
        self.toolbar.addAction(app.actions.openAction)
        self.toolbar.addAction(app.actions.makeDirAction)
        self.toolbar.addAction(app.actions.parentAction)
        self.toolbar.addAction(app.actions.insertAction)
        self.toolbar.addAction(app.actions.extractAction)
        self.toolbar.addAction(app.actions.deleteAction)
