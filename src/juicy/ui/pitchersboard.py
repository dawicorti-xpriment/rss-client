import os

from PySide import QtCore
from PySide import QtGui
from PySide import QtWebKit

import juicy
from juicy.core.config import config
from juicy.core.bridge import Bridge


class PitchersBoard(QtGui.QDialog):

    def __init__(self, parent):
        super(PitchersBoard, self).__init__(parent)
        conf = config.get('pitchersboard')
        self.setFixedSize(conf['width'], conf['height'])
        juicy.mq.listen('pitchersboard:open', self.open)
        self.loadwebview()

    def loadwebview(self):
        rect = self.geometry()
        self.webview = QtWebKit.QWebView(self)
        self.webview.setGeometry(0, 0, rect.width(), rect.height())
        self.webview.load(
            QtCore.QUrl(
                'file:///' + os.path.join(
                    juicy.rootpath,
                    'pitchersboard.html'
                ).lstrip('/').replace('\\', '/')
            )
        )
        self.webview.page().mainFrame().addToJavaScriptWindowObject(
            'bridge',
            Bridge()
        )

    def open(self, message):
        self.show()