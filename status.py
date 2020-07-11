from PyQt5.QtWidgets import QLabel, QStatusBar


class Status():
    def __init__(self, app):
        self.statusBarMessage = QLabel()
        self.statusBarMessage.setText('No file open')

        self.statusBar = QStatusBar()
        self.statusBar.addWidget(self.statusBarMessage)

        app.setStatusBar(self.statusBar)

    def setText(self, text):
        self.statusBarMessage.setText(text)
