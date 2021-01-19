import maya.api.OpenMaya as om
import maya.cmds as mc
import sys


def maya_useNewAPI():
    '''
    This function indicates maya that the api used is 2.0
    '''
    pass


class HelloWorldCmd(om.MPxCommand):
    COMMAND_NAME = "HelloWorld"

    def __init__(self):
        super(HelloWorldCmd, self).__init__()

    def doIt(self, args):
        print("Hellow World")

    @classmethod
    def creator(cls):
        return HelloWorldCmd()


def initializePlugin(plugin):  # parameter is mobject - plugin

    vendor = "Deepak Rajan"
    version = "1.0.0"

    plugin_fn = om.MFnPlugin(plugin, vendor, version)
    try:

        plugin_fn.registerCommand(HelloWorldCmd.COMMAND_NAME, HelloWorldCmd.creator)

    except:
        om.MGlobal.displayError("Faild to register: {0}".format(HelloWorldCmd))


def uninitializePlugin(plugin):
    plugin_fn = om.MFnPlugin(plugin)
    try:

        plugin_fn.deregisterCommand(HelloWorldCmd.COMMAND_NAME)
    except:
        om.MGlobal.displayError("Faild to de-register: {0}".format(HelloWorldCmd))