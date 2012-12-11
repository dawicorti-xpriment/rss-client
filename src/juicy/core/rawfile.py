import os
import requests

from PySide import QtCore


class RawFile(QtCore.QThread):

    def __init__(self, repository, version, subpath):
        super(RawFile, self).__init__()
        self._repository = repository
        self._version = version
        self._subpath = subpath

    def run(self):
        response = requests.get(
            'https://raw.github.com/%s/%s/%s' % (
                self._repository,
                self._version,
                self._subpath
            )
        )
        if not os.path.exists(os.path.dirname(self._destpath)):
            os.makedirs(os.path.dirname(self._destpath))
        with open(self._destpath, 'wb') as destfile:
            destfile.write(response.content)

    def downloaded(self):
        return self.isFinished()

    def download(self, destpath):
        self._destpath = destpath
        self.start()
