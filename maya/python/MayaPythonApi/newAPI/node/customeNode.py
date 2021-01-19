import maya.api.OpenMaya as om
import maya.cmds as mc

def maya_useNewAPI():
    '''
    Using maya new API 2.0
    :return:
    '''

class MultiplyNode(om.MPxNode):

    TYPE_NAME = "gMultiply"
    TYPE_ID = om.MTypeId(0x0007f7f7)

    def __init__(self):
        super(MultiplyNode, self).__init__()

    def compute(self, plug, data):
        pass


    @classmethod
    def creator(cls):
        return MultiplyNode()

    @classmethod
    def initialize(cls):
        pass

def initializePlugin(plugin):
    '''
    Entry point for the plugin
    :param plugin:
    :return:
    '''
    vendor = "Deepak Rajan"
    version = "1.0.0"

    plugin_fn = om.MFnPlugin(plugin, vendor, version)

    try:
        plugin_fn.registerNode(MultiplyNode.TYPE_NAME, MultiplyNode.TYPE_ID,
                               MultiplyNode.creator,  # functin/method that returns new instance of class
                               MultiplyNode.initialize,  # function/method that will initialize all attributes of node
                               om.MPxNode.kDependNode  # type of node to be registered.
                               )
    except:
        om.MGlobal.displayError("Failed to register: {0}".format(MultiplyNode.TYPE_NAME))

def uninitializePlugin(plugin):

    plugin_fn = om.MFnPlugin(plugin)

    try:
       plugin_fn.deregisterNode(MultiplyNode.TYPE_ID)
    except:
        om.MGlobal.displayError("Faild to de-register: {0}".format(MultiplyNode.TYPE_NAME))