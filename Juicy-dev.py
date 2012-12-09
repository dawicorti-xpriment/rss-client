import os
import sys
sys.path.append(
    os.path.join(
        os.path.dirname(__file__),
        'src'
    )
)

from PySide import QtGui
from juicy.ui.mainwindow import MainWindow

app = QtGui.QApplication(sys.argv)
mainwindow = MainWindow()
app.exec_()
