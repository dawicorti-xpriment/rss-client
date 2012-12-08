import json

from PySide import QtGui
from PySide import QtCore

import juicy


class Bridge(QtCore.QObject):

    signal = QtCore.Signal(str)

    def __init__(self):
        super(Bridge, self).__init__()

    @QtCore.Slot(str)
    def listen(self, name):
        juicy.mq.listen(name, self.on_message)

    def on_message(self, message):
        self.signal.emit(json.dumps(message))

    @QtCore.Slot(str)
    def send(self, raw):
        message = json.loads(raw)
        juicy.mq.send(message)
