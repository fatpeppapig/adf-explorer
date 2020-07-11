from PyQt5.QtWidgets import QListView, QAbstractItemView
from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt


class Browser():
    def __init__(self, app):
        self.listViewModel = QStandardItemModel()

        self.app = app

        self.listView = QListView(app)
        self.listView.move(15, 145)
        self.listView.setFixedSize(app.width - 30, app.height - 190)
        self.listView.setModel(self.listViewModel)
        self.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listView.doubleClicked.connect(self.processItem)
        self.listView.keyPressEvent = self.keyPressEvent
        self.listView.selectionModel().selectionChanged.connect(self.selectionChanged)

    def populate(self, entries):
        self.listViewModel.clear()

        for entry in entries:
            item = QStandardItem(QIcon(
                'icons/' +
                ('file.png' if entry['type'] == 'file' else 'folder.png')
            ), entry['name'])

            item.setData(entry)
            self.listViewModel.appendRow(item)

    def processItem(self):
        if self.item.data()['type'] == 'dir':
            self.app.navigateDown(self.selectedItem())
        else:
            self.app.extract()

    def keyPressEvent(self, event):
        super(QListView, self.listView).keyPressEvent(event)

        if event.key() == Qt.Key_Return:
            self.processItem()

    def deselect(self):
        self.item = None
        self.app.disableFileActions()

    def selectedItem(self):
        return self.item.text() if self.item else None

    def selectionChanged(self, selected, deselected):
        if len(selected.indexes()):
            modelIndex = selected.indexes()[0]

            self.item = modelIndex.model().item(modelIndex.row())
            self.app.enableFileActions()
        else:
            self.deselect()
