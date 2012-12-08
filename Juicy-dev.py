import os
import sys
sys.path.append(
    os.path.join(
        os.path.dirname(__file__),
        'src'
    )
)

from PyQt4 import QtGui
from juicy.ui.history import History

app = QtGui.QApplication(sys.argv)
history = History()
history.show()
app.exec_()
