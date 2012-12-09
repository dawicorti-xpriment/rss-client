import os
import sys


sys.path.append(
    os.path.join(
        os.path.dirname(__file__),
        'src'
    )
)

from PySide import QtGui
from juicy.ui.juice import Juice

app = QtGui.QApplication(sys.argv)
juice = Juice()
app.exec_()
