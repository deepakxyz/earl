from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2 import QtGui
from shiboken2 import wrapInstance
import sys

import maya.OpenMayaUI as omui
import os
import random
import maya.cmds as mc

def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr),QtWidgets.QWidget)
    
def mayaMainWindow():
    mainWindowPtr = omui.MQtUtil.mainWindow()
    mainWindow = wrapInstance(long(mainWindowPtr), QtWidgets.QMainWindow)
    return mainWindow
    # TODO: value and it cannot be done in the same direction

class Random(QtWidgets.QDialog):
    def __init__(self):
        super(Random, self).__init__(mayaMainWindow())
        
        self.setWindowTitle("Grey Randomizer")
        self.setMaximumHeight(100)
        self.setMaximumWidth(300)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        
        self.create_widget()
        self.create_layout()
        self.createConnections()
        
    def create_widget(self):
        self.tCheckBox = QtWidgets.QCheckBox('Translate')
        self.XminXmax = QtWidgets.QLabel('xMax | xMin')
        self.le_Tx_min = QtWidgets.QLineEdit('-0.01')
        self.le_Tx_max = QtWidgets.QLineEdit('0.01')
        self.le_Tx_zero = QtWidgets.QPushButton('0')
        
        self.YminYmax = QtWidgets.QLabel('yMax | yMin')
        self.le_Ty_min = QtWidgets.QLineEdit('-0.01')
        self.le_Ty_max = QtWidgets.QLineEdit('0.01')
        self.le_Ty_zero = QtWidgets.QPushButton('0')
        
        self.ZminZmax = QtWidgets.QLabel('zMax | zMin')
        self.le_Tz_min = QtWidgets.QLineEdit('-0.01')
        self.le_Tz_max = QtWidgets.QLineEdit('0.01')
        self.le_Tz_zero = QtWidgets.QPushButton('0')
        
        #Roate
        self.rCheckBox = QtWidgets.QCheckBox('Rotate')
        self.XminXmax_Rotate= QtWidgets.QLabel('xMax | xMin')
        self.le_Rx_min = QtWidgets.QLineEdit('-1.5')
        self.le_Rx_max = QtWidgets.QLineEdit('1.5')
        self.le_Rx_zero = QtWidgets.QPushButton('0')

        self.YminYmax_Rotate = QtWidgets.QLabel('yMax | yMin')
        self.le_Ry_min = QtWidgets.QLineEdit('-1.5')
        self.le_Ry_max = QtWidgets.QLineEdit('1.5')
        self.le_Ry_zero = QtWidgets.QPushButton('0')

        self.ZminZmax_Rotate = QtWidgets.QLabel('zMax | zMin')
        self.le_Rz_min = QtWidgets.QLineEdit('-1.5')
        self.le_Rz_max = QtWidgets.QLineEdit('1.5')
        self.le_Rz_zero = QtWidgets.QPushButton('0')
        
        #Scale
        
        self.sCheckBox = QtWidgets.QCheckBox('Scale')
        self.sLinkCheckBox = QtWidgets.QCheckBox('Link Scale Attributes')
        self.XminXmax_scale= QtWidgets.QLabel('xMax | xMin')
        self.le_Sx_min = QtWidgets.QLineEdit('0.9')
        self.le_Sx_max = QtWidgets.QLineEdit('1.1')
        self.le_Sx_zero = QtWidgets.QPushButton('0')

        self.YminYmax_scale = QtWidgets.QLabel('yMax | yMin')
        self.le_Sy_min = QtWidgets.QLineEdit('0.9')
        self.le_Sy_max = QtWidgets.QLineEdit('1.1')
        self.le_Sy_zero = QtWidgets.QPushButton('0')

        self.ZminZmax_scale = QtWidgets.QLabel('zMax | zMin')
        self.le_Sz_min = QtWidgets.QLineEdit('0.9')
        self.le_Sz_max = QtWidgets.QLineEdit('1.1')
        self.le_Sz_zero = QtWidgets.QPushButton('0')
        
        #Randomize Button
        self.RandButton = QtWidgets.QPushButton('Randomize')
        
    def create_layout(self):

        self.VLayout = QtWidgets.QVBoxLayout(self)
        self.VLayout.addWidget(self.tCheckBox)
        self.HLayout_translate_x = QtWidgets.QHBoxLayout()
        self.HLayout_translate_x.addWidget(self.XminXmax)
        self.HLayout_translate_x.addWidget(self.le_Tx_min)
        self.HLayout_translate_x.addWidget(self.le_Tx_max)
        #self.HLayout_translate_x.addWidget(self.le_Tx_zero)
        
        self.HLayout_translate_y = QtWidgets.QHBoxLayout()
        self.HLayout_translate_y.addWidget(self.YminYmax)
        self.HLayout_translate_y.addWidget(self.le_Ty_min)
        self.HLayout_translate_y.addWidget(self.le_Ty_max)
        #self.HLayout_translate_y.addWidget(self.le_Ty_zero)
        
        
        self.HLayout_translate_z = QtWidgets.QHBoxLayout()
        self.HLayout_translate_z.addWidget(self.ZminZmax)
        self.HLayout_translate_z.addWidget(self.le_Tz_min)
        self.HLayout_translate_z.addWidget(self.le_Tz_max)
        #self.HLayout_translate_z.addWidget(self.le_Tz_zero)
        
        
        
        self.VLayout.addLayout(self.HLayout_translate_x)
        self.VLayout.addLayout(self.HLayout_translate_y)
        self.VLayout.addLayout(self.HLayout_translate_z)
        
        #Rotate
        
        self.VLayout.addWidget(self.rCheckBox)
        self.HLayout_rotate_x = QtWidgets.QHBoxLayout()
        self.HLayout_rotate_x.addWidget(self.XminXmax_Rotate)
        self.HLayout_rotate_x.addWidget(self.le_Rx_min)
        self.HLayout_rotate_x.addWidget(self.le_Rx_max)
        #self.HLayout_rotate_x.addWidget(self.le_Rx_zero)


        self.HLayout_rotate_y = QtWidgets.QHBoxLayout()
        self.HLayout_rotate_y.addWidget(self.YminYmax_Rotate)
        self.HLayout_rotate_y.addWidget(self.le_Ry_min)
        self.HLayout_rotate_y.addWidget(self.le_Ry_max)
        #self.HLayout_rotate_y.addWidget(self.le_Ry_zero)


        self.HLayout_rotate_z = QtWidgets.QHBoxLayout()
        self.HLayout_rotate_z.addWidget(self.ZminZmax_Rotate)
        self.HLayout_rotate_z.addWidget(self.le_Rz_min)
        self.HLayout_rotate_z.addWidget(self.le_Rz_max)
        #self.HLayout_rotate_z.addWidget(self.le_Rz_zero)



        self.VLayout.addLayout(self.HLayout_rotate_x)
        self.VLayout.addLayout(self.HLayout_rotate_y)
        self.VLayout.addLayout(self.HLayout_rotate_z)
        
        
        #Scale
        
        
        self.HLayout_scale_link = QtWidgets.QHBoxLayout()
        self.HLayout_scale_link.addWidget(self.sCheckBox)
        self.HLayout_scale_link.addWidget(self.sLinkCheckBox)
        self.VLayout.addLayout(self.HLayout_scale_link)
        
        self.HLayout_scale_x = QtWidgets.QHBoxLayout()
        self.HLayout_scale_x.addWidget(self.XminXmax_scale)
        self.HLayout_scale_x.addWidget(self.le_Sx_min)
        self.HLayout_scale_x.addWidget(self.le_Sx_max)
        #self.HLayout_scale_x.addWidget(self.le_Sx_zero)


        self.HLayout_scale_y = QtWidgets.QHBoxLayout()
        self.HLayout_scale_y.addWidget(self.YminYmax_scale)
        self.HLayout_scale_y.addWidget(self.le_Sy_min)
        self.HLayout_scale_y.addWidget(self.le_Sy_max)
        #self.HLayout_scale_y.addWidget(self.le_Sy_zero)


        self.HLayout_scale_z = QtWidgets.QHBoxLayout()
        self.HLayout_scale_z.addWidget(self.ZminZmax_scale)
        self.HLayout_scale_z.addWidget(self.le_Sz_min)
        self.HLayout_scale_z.addWidget(self.le_Sz_max)
        #self.HLayout_scale_z.addWidget(self.le_Sz_zero)



        self.VLayout.addLayout(self.HLayout_scale_x)
        self.VLayout.addLayout(self.HLayout_scale_y)
        self.VLayout.addLayout(self.HLayout_scale_z)
        self.VLayout.addWidget(self.RandButton)
        
        
        
        
    def createConnections(self):
        self.RandButton.clicked.connect(self.grey_randomizer)
        
    def setZero(self):
        self.le_Tx_min.setText('0')
        self.le_Tx_max.setText('0')
        
    def grey_randomizer(self):
        #translate
        le_Tx_min = float(self.le_Tx_min.text())
        le_Tx_max = float(self.le_Tx_max.text())
        le_Ty_min = float(self.le_Ty_min.text())
        le_Ty_max = float(self.le_Ty_max.text())
        le_Tz_min = float(self.le_Tz_min.text())
        le_Tz_max = float(self.le_Tz_max.text())
        
        
        #roate
        le_Rx_min = float(self.le_Rx_min.text())
        le_Rx_max = float(self.le_Rx_max.text())
        le_Ry_min = float(self.le_Ry_min.text())
        le_Ry_max = float(self.le_Ry_max.text())
        le_Rz_min = float(self.le_Rz_min.text())
        le_Rz_max = float(self.le_Rz_max.text())
        
        #scale
        le_Sx_min = float(self.le_Sx_min.text())
        le_Sx_max = float(self.le_Sx_max.text())
        le_Sy_min = float(self.le_Sy_min.text())
        le_Sy_max = float(self.le_Sy_max.text())
        le_Sz_min = float(self.le_Sz_min.text())
        le_Sz_max = float(self.le_Sz_max.text())
        
        translateSignal = self.tCheckBox.isChecked()
        rotateSignal = self.rCheckBox.isChecked()
        scaleSignal = self.sCheckBox.isChecked()
        scaleLinkSignal = self.sLinkCheckBox.isChecked()
        
        
        selection = mc.ls(selection = True)
        mc.undoInfo(openChunk = True)
        try:
            for object in selection:
                
                #translate
                if translateSignal:
                    
                    tX = random.uniform(le_Tx_min, le_Tx_max)
                    tY = random.uniform(le_Ty_min, le_Ty_max)
                    tZ = random.uniform(le_Tz_min, le_Tz_max)
                    mc.move(tX, tY, tZ, object, r = True, os = True, wd = True)
                else:
                    pass
                    #print('Translate slot is Locked')
                    
                #rotate
                if rotateSignal:
                    
                    rX = random.uniform(le_Rx_min, le_Rx_max)
                    rY = random.uniform(le_Ry_min, le_Ry_max)
                    rZ = random.uniform(le_Rz_min, le_Rz_max)
                    mc.rotate(rX, rY, rZ, object, r = True)
                    
                else:
                    pass
                    #print('Rotate slot is Locked')
                
                #scale
                if scaleSignal:
                    sX = random.uniform(le_Sx_min, le_Sx_max)
                    sY = random.uniform(le_Sy_min, le_Sy_max)
                    sZ = random.uniform(le_Sz_min, le_Sz_max)
                    mc.scale(sX, sY, sZ, object, r = True)
                    print('Single Signal')
                    
                else:
                    pass
                    #print('Scale slot is Locked')
                    
                if scaleLinkSignal:
                    sU = random.uniform(le_Sx_min, le_Sx_max)
                    
                    mc.scale(sU, sU, sU, object, r = True)
                    print('Double Signal')
                    
                else:
                    pass
            
        finally:
            mc.undoInfo(closeChunk = True)
                
        
        
if __name__ == "__main__":
    
    try:
        RandDialog.close()
        Random.deleteLater()
    except:
        pass
        
        
        
    RandDialog = Random()
    RandDialog.show()


