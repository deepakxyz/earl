from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2 import QtGui
from shiboken2 import wrapInstance
import sys

import maya.OpenMayaUI as omui
import maya.cmds as mc
import maya.mel as mm


def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)


def mayaMainWindow():
    mainWindowPtr = omui.MQtUtil.mainWindow()
    mainWindow = wrapInstance(long(mainWindowPtr), QtWidgets.QMainWindow)
    return mainWindow


class MelExc(QtWidgets.QDialog):
    def __init__(self):
        super(MelExc, self).__init__(mayaMainWindow())
        #self.setFixedSize(411, 80)
        self.setWindowTitle("MEL Executor")
        self.setMinimumHeight(50)
        self.setMinimumWidth(400)
        self.setMaximumHeight(100)

        self.setWindowFlags(self.windowFlags() ^
                            QtCore.Qt.WindowContextHelpButtonHint)

        self.create_widget()
        self.create_layout()

    def create_widget(self):
        self.melLable = QtWidgets.QLabel('MEL')
        self.melLE = QtWidgets.QLineEdit()
        self.melLE.setStyleSheet(
            "padding: 5 2px;" "selection-background-color:rgb(133, 118, 90)")
        # self.melLE.setFont(QtGui.QFont("Tahoma",10))
        self.melLE.returnPressed.connect(self.mel_exc)

    def create_layout(self):
        self.HLayout_mel = QtWidgets.QHBoxLayout(self)
        self.HLayout_mel.addWidget(self.melLable)
        self.HLayout_mel.addWidget(self.melLE)

    def mel_exc(self):
        cmd = str(self.melLE.text())
        mm.eval(cmd)
        self.melLE.setText('')


if __name__ == "__main__":

    try:
        MelExcDialog.close()
        MelExc.deleteLater()
    except:
        pass

    MelExcDialog = MelExc()
    MelExcDialog.show()
