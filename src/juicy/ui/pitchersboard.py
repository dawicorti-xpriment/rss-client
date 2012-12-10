import os

from PySide import QtCore
from PySide import QtGui
from PySide import QtWebKit

import juicy
from juicy.core.config import config
from juicy.core.bridge import Bridge
from juicy.ui.webpage import WebPage


class PitchersBoard(QtGui.QDialog):

    def __init__(self, parent):
        super(PitchersBoard, self).__init__(parent)
        self.setFixedSize(
            config.get('pitchersboard_width'),
            config.get('pitchersboard_height')
        )
        juicy.mq.listen('pitchersboard:open', self.open)
        self.loadwebview()

    def loadwebview(self):
        rect = self.geometry()
        self.webview = QtWebKit.QWebView(self)
        self.webview.setPage(WebPage('pitchers-list'))
        self.webview.settings().setAttribute(
            QtWebKit.QWebSettings.LocalContentCanAccessRemoteUrls,
            True
        )
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
