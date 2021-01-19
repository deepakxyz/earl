import maya.api.OpenMaya as om
import maya.cmds as mc
import sys


# this function indicates maya that the api used is 2.0
def maya_useNewAPI():
    pass


def initializePlugin(plugin):  # parameter is mobject - plugin

    vendor = "Deepak Rajan"
    version = "1.0.0"

    om.MFnPlugin(plugin, vendor, version)


def uninitializePlugin(plugin):
    pass