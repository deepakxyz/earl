import maya.api.OpenMaya as om

def maya_useNewAPI():
    '''
    This function indicates maya that the api used is 2.0
    This is very important to run in the new API
    '''
    pass

class SimpleCmd(om.MPxCommand):

    COMMAND_NAME = "simpleCmd"

    def __init__(self):
        super(SimpleCmd, self).__init__()

    def doIt(self, arg_list):
        self.displayInfo("Info: dotIt() method called")

    def undoIt(self):
        self.displayInfo("Info: undoIt() method called")

    def redoIt(self):
        self.displayInfo("Info: redoIt() method called")

    def isUndoable(self):
        self.displayInfo("Info: isUndoable() method called")
        return True


    @classmethod
    def creator(cls):
        cls.displayInfo("Info: creator() static method called")

        return SimpleCmd()

    @classmethod
    def create_syntax(cls):
        cls.displayInfo("Info: create_syntax() static method called")

        syntax = om.MSyntax()

        # add flags here
        return syntax

def initializePlugin(plugin):

    vendor = "Deepak Rajan"
    version = "1.0.0"

    plugin_fn = om.MFnPlugin(plugin, vendor, version)
    try:
        plugin_fn.registerCommand(SimpleCmd.COMMAND_NAME, SimpleCmd.creator, SimpleCmd.create_syntax)
    except:
        om.MGlobal.displayError("Failed to register command: {0}".format(SimpleCmd.COMMAND_NAME))

def uninitializePlugin(plugin):

    plugin_fn = om.MFnPlugin(plugin)
    try:
        plugin_fn.deregisterCommand(SimpleCmd.COMMAND_NAME)
    except:
        om.MGlobal.displayError("Failed to de-register command: {0}".format(SimpleCmd.COMMAND_NAME))