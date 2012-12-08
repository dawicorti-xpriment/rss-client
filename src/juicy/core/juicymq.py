import Queue

from PySide import QtCore


class JuicyMQ(object):

    def __init__(self):
        self._queue = Queue.Queue()
        self._callbacks = {}

    def run(self):
        self._timer = QtCore.QTimer()
        self._timer.timeout.connect(self.on_tick)
        self._timer.start(0.04)

    def on_tick(self):
        self.read_messages()

    def read_messages(self):
        message = None
        try:
            message = self._queue.get_nowait()
        except Queue.Empty:
            pass
        if type(message) is dict \
                and 'name' in message \
                and message['name'] in self._callbacks:
            for callback in self._callbacks[message['name']]:
                callback(message)

    def listen(self, name, callback):
        if not name in self._callbacks:
            self._callbacks[name] = []
        if not callback in self._callbacks[name]:
            self._callbacks[name].append(callback)

    def send(self, message):
        self._queue.put_nowait(message)
