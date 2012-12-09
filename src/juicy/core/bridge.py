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
        juicy.mq.listen(name, Bridge.on_message)

    @staticmethod
    def on_message(message):
        Bridge.signal.emit(json.dumps(message))

    @QtCore.Slot(str)
    def send(self, raw):
        message = json.loads(raw)
        juicy.mq.send(message)
