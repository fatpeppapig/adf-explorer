from PyQt5.QtWidgets import QLabel, QLineEdit


class Path():
    def __init__(self, app):
        self.app = app

        label = QLabel('Path:', app)
        label.move(15, 100)

        self.pathInput = QLineEdit(app)
        self.pathInput.move(50, 100)
        self.pathInput.setFixedWidth(app.width - 65)
        self.pathInput.editingFinished.connect(self.pathEnter)
        self.disable()

    def pathEnter(self):
        try:
            self.app.navigate(self.pathInput.text())
        except:
            self.pathInput.setText(self.app.adf.node)

    def enable(self):
        self.pathInput.setDisabled(False)

    def disable(self):
        self.pathInput.setDisabled(True)

    def setText(self, text):
        self.pathInput.setText(text)

    def text(self):
        self.pathInput.text()
