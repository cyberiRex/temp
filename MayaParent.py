from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from shiboken2 import wrapInstance
def getMayaWindow():
    # Get Maya window
    mayaMainWindowPtr = omui.MQtUtil.mainWindow()
    mayaMainWindow = wrapInstance(long(mayaMainWindowPtr), QMainWindow)
    return mayaMainWindow
    
class TestClass(QMainWindow,UI.Ui_MainWindow):
    def __init__(self):
        super(TestClass, self).__init__(getMayaWindow())
        self.setupUi(self)
    
        # Get Maya window
        mayaMainWindowPtr = omui.MQtUtil.mainWindow()
        mayaMainWindow = wrapInstance(long(mayaMainWindowPtr), QMainWindow)
    
        # Set main window
        QMainWindow(mayaMainWindow, Qt.Window)
