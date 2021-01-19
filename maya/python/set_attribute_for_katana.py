from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2 import QtGui
from shiboken2 import wrapInstance
import sys
import os

import maya.OpenMayaUI as omui
import maya.cmds as mc


def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)


def mayaMainWindow():
    mainWindowPtr = omui.MQtUtil.mainWindow()
    mainWindow = wrapInstance(long(mainWindowPtr), QtWidgets.QMainWindow)
    return mainWindow


class AttSetter(QtWidgets.QDialog):
    def __init__(self):
        super(AttSetter, self).__init__(mayaMainWindow())
        self.setFixedSize(411, 180)
        self.setWindowTitle("Attribute Setter")
        self.setMaximumHeight(100)
        self.setMaximumWidth(300)
        self.setWindowFlags(self.windowFlags() ^
                            QtCore.Qt.WindowContextHelpButtonHint)

        self.create_widget()
        self.create_layout()
        self.createConnections()

    def create_widget(self):
        # Attribute Name
        self.attribName = QtWidgets.QLabel('Attribute Name')
        self.attribName_le = QtWidgets.QLineEdit('MatTag')
        self.attribName_le.setStyleSheet(
            "background-color: rgb(28,28,28); color: rgb(222, 222, 222);")

        # Attribute Add | Delete Button
        self.attrib_add_btn = QtWidgets.QPushButton('Add')
        self.attrib_del_btn = QtWidgets.QPushButton('Delete')

        # Attribute Value
        self.attribValue = QtWidgets.QLabel('Attribute Value')
        self.attribValue_le = QtWidgets.QLineEdit('lambert')

        # Attribute Set | Remove Button
        self.attrib_set_btn = QtWidgets.QPushButton('Set')
        self.attrib_remove_btn = QtWidgets.QPushButton('Remove')

        # Get Current Value
        self.getAttrib = QtWidgets.QLabel('default_value')
        self.getAttrib.setStyleSheet("color: rgb(204, 141, 59);")
        self.getAttrib_btn = QtWidgets.QPushButton('Get')
        self.getAttrib_btn.setStyleSheet(
            "background-color: rgb(86, 111, 117); color: rgb(222, 222, 222);")

    def create_layout(self):
        self.VLayout = QtWidgets.QVBoxLayout(self)
        self.HLayout_attribName = QtWidgets.QHBoxLayout()
        self.HLayout_attribName.addWidget(self.attribName)
        self.HLayout_attribName.addWidget(self.attribName_le)

        self.HLayout_add_del_btn = QtWidgets.QHBoxLayout()
        self.HLayout_add_del_btn.addWidget(self.attrib_add_btn)
        self.HLayout_add_del_btn.addWidget(self.attrib_del_btn)

        self.HLayout_attribValue = QtWidgets.QHBoxLayout()
        self.HLayout_attribValue.addWidget(self.attribValue)
        self.HLayout_attribValue.addWidget(self.attribValue_le)

        self.HLayout_set_remove_btn = QtWidgets.QHBoxLayout()
        self.HLayout_set_remove_btn.addWidget(self.attrib_set_btn)
        self.HLayout_set_remove_btn.addWidget(self.attrib_remove_btn)

        self.HLayout_current_value = QtWidgets.QHBoxLayout()
        self.HLayout_current_value.addWidget(self.getAttrib)
        self.HLayout_current_value.addWidget(self.getAttrib_btn)

        self.VLayout.addLayout(self.HLayout_attribName)
        self.VLayout.addLayout(self.HLayout_add_del_btn)
        self.VLayout.addLayout(self.HLayout_attribValue)
        self.VLayout.addLayout(self.HLayout_set_remove_btn)
        self.VLayout.addLayout(self.HLayout_current_value)

    def createConnections(self):
        self.attrib_add_btn.clicked.connect(self.add_attr)
        self.attrib_del_btn.clicked.connect(self.del_attr)
        self.attrib_set_btn.clicked.connect(self.set_attr)
        self.attrib_remove_btn.clicked.connect(self.rem_attr)
        self.getAttrib_btn.clicked.connect(self.get_attr)

    def objselection(self):
        selection = mc.ls(selection=True)
        return selection

    # Add attribute

    def add_attr(self):
        selection = self.objselection()

        # Value
        attributeName = str(self.attribName_le.text())
        attributeValue = str(self.attribValue_le.text())
        DEFAULT_VALUE = "lambert"

        for obj in selection:
            # check if attribute exists
            if mc.attributeQuery(attributeName, node=obj, exists=True):
                print("Attribute already exists")
            else:
                mc.addAttr(obj, longName=attributeName, dataType="string")

                # set default
                mc.setAttr(obj + "." + attributeName,
                           attributeValue, type='string')

    # Delete Attribute
    def del_attr(self):
        selection = self.objselection()

        # Value
        attributeName = str(self.attribName_le.text())
        attributeValue = str(self.attribValue_le.text())

        for obj in selection:
            if mc.attributeQuery(attributeName, node=obj, exists=True):
                mc.deleteAttr(obj, at=attributeName)

    def set_attr(self):
        selection = self.objselection()

        # Value
        attributeName = str(self.attribName_le.text())
        attributeValue = str(self.attribValue_le.text())

        for obj in selection:
            if mc.attributeQuery(attributeName, node=obj, exists=True):
                mc.setAttr(obj + "." + attributeName,
                           attributeValue, type="string")

    def rem_attr(self):
        selection = self.objselection()

        # Value
        attributeName = str(self.attribName_le.text())
        remove_attr = "None"

        for obj in selection:
            if mc.attributeQuery(attributeName, node=obj, exists=True):
                mc.setAttr(obj + "." + attributeName,
                           remove_attr, type="string")

    def get_attr(self):
        selection = self.objselection()

        # Value
        attributeName = str(self.attribName_le.text())
        get_attr = mc.getAttr(selection[-1]+"."+attributeName)
        self.getAttrib.setText(get_attr)


if __name__ == "__main__":

    try:
        AttSetterDialog.close()
        AttSetter.deleteLater()
    except:
        pass

    AttSetterDialog = AttSetter()
    AttSetterDialog.show()
