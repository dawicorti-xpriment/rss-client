import logging

from PyQt4 import QtWebKit


class RootPage(QtWebKit.QWebPage):

    def __init__(self):
        super(RootPage, self).__init__()
        self._logger = logging.getLogger()
        self._logger.setLevel(logging.DEBUG)
        self._logger.addHandler(logging.StreamHandler())

    def javaScriptConsoleMessage(self, msg, line, source):
        self._logger.debug('[ROOTPAGE] %s line %d: %s' % (source, line, msg))