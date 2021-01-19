import maya.api.OpenMaya as om

def maya_useNewAPI():
    '''
    This function indicates maya that the api used is 2.0
    This is very important to run in the new API
    '''
    pass

class SimpleCmd(om.MPxCommand):

    COMMAND_NAME = "simpleCmd"

    VERSION_FLAG = ["-v", "-version"]
    NAME_FLAG = ["-n", "-name"]

    def __init__(self):
        super(SimpleCmd, self).__init__()

        self.undoable = False

    def doIt(self, arg_list):
        try:
            arg_db = om.MArgDatabase(self.syntax(), arg_list)
        except:
            self.displayError("Error parsing arguments")
            raise
        version_flag_enabled = arg_db.isFlagSet(SimpleCmd.VERSION_FLAG[0])
        if version_flag_enabled:
            # self.displayInfo("Version Flag enabled - Version: 1.0.0")
            self.setResult("1.0.0")
            self.undoable = True # set undoable for particular function
        else:
            name = "SimpleCmd"

            if arg_db.isFlagSet(SimpleCmd.NAME_FLAG[0]):
                name = arg_db.flagArgumentString(SimpleCmd.NAME_FLAG[0], 0)

            self.displayInfo("Hello {0}".format(name))

    def undoIt(self):
        pass

    def redoIt(self):
        pass

    def isUndoable(self):
        return self.undoable


    @classmethod
    def creator(cls):

        return SimpleCmd()

    @classmethod
    def create_syntax(cls):

        syntax = om.MSyntax()

        syntax.addFlag(SimpleCmd.VERSION_FLAG[0], SimpleCmd.VERSION_FLAG[1])
        syntax.addFlag(SimpleCmd.NAME_FLAG[0], SimpleCmd.NAME_FLAG[1],om.MSyntax.kString) # add new argument form the user

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