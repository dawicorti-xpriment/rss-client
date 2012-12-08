import os

from PySide import QtGui
from PySide import QtCore
from PySide import QtWebKit

import juicy
from juicy.core.config import config
from juicy.core.bridge import Bridge


class MainWindow(QtGui.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        juicy.mq.run()
        self.tray_icon = QtGui.QSystemTrayIcon(
            QtGui.QIcon(
                os.path.join(
                    juicy.assetspath,
                    'images',
                    'juicy.png'
                )
            ),
            self
        )
        self.tray_icon.activated.connect(self.show)
        self.tray_icon.show()
        rect = self.geometry()
        conf = config.get('history')
        if conf.get('x') is not None:
            rect.setX(conf.get('x'))
        if conf.get('y') is not None:
            rect.setY(conf.get('y'))
        width = conf.get('width')
        height = conf.get('height')
        rect.setWidth(width)
        rect.setHeight(height)
        self.setGeometry(rect)
        self.setMaximumWidth(width)
        self.setMinimumWidth(width)
        self.loadwebview()

    def loadwebview(self):
        rect = self.geometry()
        self.webview = QtWebKit.QWebView(self)
        self.webview.setGeometry(0, 0, rect.width(), rect.height())
        self.webview.load(
            QtCore.QUrl(
                'file:///' + os.path.join(
                    juicy.rootpath,
                    'index.html'
                ).lstrip('/').replace('\\', '/')
            )
        )
        self.bridge = Bridge()
        self.webview.page().mainFrame().addToJavaScriptWindowObject(
            'bridge',
            self.bridge
        )

    def resizeEvent(self, event):
        rect = self.geometry()
        self.webview.setGeometry(0, 0, rect.width(), rect.height())
        conf = config.get('history')
        conf['height'] = rect.height()
        config.save()

    def moveEvent(self, event):
        rect = self.geometry()
        conf = config.get('history')
        conf['x'] = rect.x()
        conf['y'] = rect.y()
        config.save()

    def closeEvent(self, event):
        juicy.mq.send({'name': 'test'})
        event.ignore()
        #self.hide()


