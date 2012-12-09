from PySide import QtWebKit

from juicy.core.config import config


class WebPage(QtWebKit.QWebPage):

    def __init__(self, name):
        super(WebPage, self).__init__()
        self._name = name

    def javaScriptConsoleMessage(self, msg, line, source):
        print ('[%s] %s line %d: %s' % (
            self._name,
            source,
            line,
            msg
        ))