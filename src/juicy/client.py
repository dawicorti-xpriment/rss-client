from PySide import QtGui

import juicy
from juicy.core import root
from juicy.core.config import Config
from juicy.core.repository import Repository
from juicy.ui.juice import Juice
from juicy.ui.pitchersboard import PitchersBoard


class JuicyClient(object):

    def __init__(self, argv=[]):
        self._app = QtGui.QApplication(argv)
        self._pitchers = root.get_installed_pitchers()
        root.copy_to_home()
        juicy.mq.listen('juice:quit', self.quit)
        juicy.mq.listen('juice:open', self.on_open_juice)
        juicy.mq.listen('config:get', self.get_config)
        juicy.mq.listen('pitchers:get', self.get_pitchers)
        self._juice = Juice()
        self._repository = Repository('dawicorti/juicy', 'stable')
        self._pitchers_board = PitchersBoard(self._juice)

    def get_config(self, message):
        if 'module' in message:
            juicy.mq.send({
                'name': 'config:send',
                'module': message['module'],
                'data': Config(message['module'] + '.json').data()
            })

    def run(self):
        self._app.exec_()

    def on_repository_downloaded(self, destpath):
        root.sync_dirs(destpath, juicy.homepath, overwrite=True)

    def on_open_juice(self, message):
        self._juice.show()
        self._repository.download(
            'src/juicy/root',
            self.on_repository_downloaded
        )

    def quit(self, message):
        self._app.quit()

    def get_pitchers(self, message):
        print 'sending pitchers'
        juicy.mq.send({
            'name': 'pitchers:send',
            'pitchers': self._pitchers
        })
