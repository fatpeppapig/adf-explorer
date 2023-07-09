from amitools.fs.ADFSVolume import ADFSVolume
from amitools.fs.blkdev.BlkDevFactory import BlkDevFactory
from amitools.fs.FileName import FileName
from amitools.fs.Imager import Imager
from amitools.tools.xdftool import make_fsstr

import os.path


class ADF():
    def __init__(self, app):
        self.app = app
        self.volume = None
        self.blkdev = None
        self.node = None
        self.path = None

    def absolutePath(self, name):
        return (self.path + '/' if self.path != '/' else '') + name

    def create(self, path):
        self.cleanUp()
        
        #NOTE: Was crashing saying unrecognize file type is I entered blankdisk, I needed blankdisk.adf
        # This code just checks and adds .adf to the end if missing.
        if not path.endswith(".adf"):
            path += ".adf"

        self.blkdev = BlkDevFactory().create(path)
        self.volume = ADFSVolume(self.blkdev)

        name = os.path.basename(path)

        self.volume.create(make_fsstr(name), dos_type=None)

    def open(self, path):
        self.cleanUp()

        self.blkdev = BlkDevFactory().open(path)
        self.volume = ADFSVolume(self.blkdev)
        self.volume.open()

    def navigate(self, path='/'):
        try:
            self.node = self.volume.get_path_name(make_fsstr(path))
        except:
            return

        self.path = path
        self.entries = [{
            'name': entry.get_file_name().get_name().__str__(),
            'type': 'dir' if entry.is_dir() else 'file'
        } for entry in self.node.get_entries_sorted_by_name()]

        self.app.updatePath(self.path)
        self.app.updateBrowser(self.entries)

    def navigateDown(self, dir):
        if self.path == '/':
            self.navigate(dir)
        else:
            self.navigate(self.path + '/' + dir)

    def parent(self):
        path = self.path.split('/')[:-1]

        if len(path) > 1:
            self.navigate(path.join('/'))
        elif len(path) == 1:
            self.navigate(path[0])
        else:
            self.navigate()

    def volumeName(self):
        return self.volume.get_volume_name().__str__()

    def volumeInfo(self):
        return self.volume.get_info().__str__()

    def extract(self, name, output):
        path = self.absolutePath(name)
        node = self.volume.get_path_name(make_fsstr(path))

        if node.is_file():
            data = node.get_file_data()
            fh = open(output, 'wb')
            fh.write(data)
            fh.close()
        elif node.is_dir():
            img = Imager(meta_mode=Imager.META_MODE_NONE)
            img.unpack_dir(node, output)

    def insert(self, input):
        name = os.path.basename(input)

        if os.path.isfile(input):
            fh = open(input, 'rb')
            data = fh.read()
            fh.close()

            self.volume.write_file(
                data, make_fsstr(self.path), make_fsstr(name))
        elif os.path.isdir(input):
            parent, name = self.volume.get_create_path_name(
                make_fsstr(self.path), make_fsstr(name))

            node = parent.create_dir(name)
            img = Imager(meta_mode=Imager.META_MODE_NONE)
            img.pack_dir(input, node)

        self.navigate(self.path)

    def makeDir(self, name):
        path = self.absolutePath(name)

        self.volume.create_dir(make_fsstr(path))
        self.navigate(self.path)

    def delete(self, name):
        path = self.absolutePath(name)

        self.volume.delete(make_fsstr(path), all=True)
        self.navigate(self.path)

    def relabel(self, name):
        self.volume.relabel(make_fsstr(name))

    def cleanUp(self):
        if self.volume:
            self.volume.close()

        if self.blkdev:
            self.blkdev.close()
