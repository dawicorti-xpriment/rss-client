import os

from PySide import QtGui
from PySide import QtCore
from PySide import QtWebKit

import juicy
from juicy.core.config import config
from juicy.core.config import Config
from juicy.core.bridge import Bridge
from juicy.ui.pitchersboard import PitchersBoard


class Juice(QtGui.QMainWindow):

    def __init__(self):
        super(Juice, self).__init__()
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
        if config.get('juice_x') is not None:
            rect.setX(config.get('juice_x'))
        if config.get('juice_y') is not None:
            rect.setY(config.get('juice_y'))
        width = config.get('juice_width')
        height = config.get('juice_height')
        rect.setWidth(width)
        rect.setHeight(height)
        self.setGeometry(rect)
        self.setMaximumWidth(width)
        self.setMinimumWidth(width)
        self.loadwebview()
        self.pitchers_board = PitchersBoard(self)
        juicy.mq.listen('juice:quit', self.quit)
        juicy.mq.listen('juice:open', self.open)
        juicy.mq.listen('config:get', self.get_config)

    def get_config(self, message):
        if 'module' in message:
            juicy.mq.send({
                'name': 'config:send',
                'module': message['module'],
                'data': Config(message['module'] + '.json').data()
            })

    def open(self, message):
        self.show()

    def loadwebview(self):
        rect = self.geometry()
        self.webview = QtWebKit.QWebView(self)
        self.webview.setGeometry(0, 0, rect.width(), rect.height())
        self.webview.load(
            QtCore.QUrl(
                'file:///' + os.path.join(
                    juicy.rootpath,
                    'juice.html'
                ).lstrip('/').replace('\\', '/')
            )
        )
        self.webview.page().mainFrame().addToJavaScriptWindowObject(
            'bridge',
            Bridge()
        )

    def resizeEvent(self, event):
        rect = self.geometry()
        self.webview.setGeometry(0, 0, rect.width(), rect.height())
        config.set('juice_height', rect.height())
        config.save()

    def moveEvent(self, event):
        rect = self.geometry()
        config.set('juice_x', rect.x())
        config.set('juice_y', rect.y())
        config.save()

    def quit(self, message):
        QtGui.QApplication.quit()

    def closeEvent(self, event):
        event.ignore()
        self.hide()
