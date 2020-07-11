class Menu():
    def __init__(self, app):
        self.menubar = app.menuBar()
        self.menubar.setNativeMenuBar(False)

        self.fileMenu = self.menubar.addMenu('File')

        self.fileMenu.addAction(app.actions.createAction)
        self.fileMenu.addAction(app.actions.openAction)
        self.fileMenu.addAction(app.actions.quitAction)
