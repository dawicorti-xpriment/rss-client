import os
import tempfile
import uuid
import requests
from PySide import QtCore

from juicy.core.rawfile import RawFile

class Repository(object):

    def __init__(self, repository, version, recursive=10):
        self._destpath = os.path.join(
            'juicy',
            tempfile.gettempdir(),
            str(uuid.uuid1())
        )
        if not os.path.exists(self._destpath):
            os.makedirs(self._destpath)
        self._version = version
        self._repository = repository
        self._recursive = recursive
        self._timer = QtCore.QTimer()
        self._timer.timeout.connect(self.on_tick)

    def download(self, subpath, callback):
        self._currentfile = None
        self._callback = callback
        self._index = 0
        self._tree = None
        self._subpath = subpath
        self._timer.start(100)

    def get_tree(self):
        try:
            response = requests.get(
                'https://api.github.com/repos/'
                + self._repository
                + '/git/trees/'
                + self._version,
                params={'recursive': self._recursive}
            )
            self._tree = response.json['tree']
        except:
            self._timer.stop()

    def get_file(self):
        if self._currentfile is None or self._currentfile.downloaded():
            path = os.path.join(
                self._destpath,
                (
                    self._tree[self._index]['path']
                )[len(self._subpath):].lstrip('/')
            )
            if self._tree[self._index]['type'] == 'tree':
                if not os.path.exists(path):
                    os.makedirs(path)
            else:
                self._currentfile = RawFile(
                    self._repository,
                    self._version,
                    self._tree[self._index]['path']
                )
                self._currentfile.download(path)
            self._index += 1

    def on_tick(self):
        if self._tree is None:
            self.get_tree()
        elif self._index >= len(self._tree):
            self._callback(self._destpath)
            self._timer.stop()
        elif not self._tree[self._index]['path'].startswith(self._subpath):
            self._index += 1
        else:
            self.get_file()
