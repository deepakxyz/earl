import maya.OpenMaya as om
import maya.OpenMayaMPx as ommpx

class BasicDeformerNode(ommpx.MPxDeformerNode):

    TYPE_NAME = "BasicDeformerNode"
    TYPE_ID = om.MTypeId(0x0007f7fC)

    def __init__(self):
        super(BasicDeformerNode, self).__init__()

    def deform(self, data_block, geo_iter, matrix, multi_index):
        '''
        :param data_block: This is MDatablock Object, this provides access to nodes attribute values
        :param geo_iter: MIt, iterator.
        :param matrix: MMatrix, world transform matrix.
        :param multi_index: integer, ex: geometry with multiple components.
        :return:
        '''
        print("TODO: deform()")

    @classmethod
    def creator(cls):
        return BasicDeformerNode()

    @classmethod
    def initialize(cls):
        pass





def initializePlugin(plugin):

    vendor = "Deepak Rajan"
    version = "1.0.0"

    plugin_fn = ommpx.MFnPlugin(plugin, vendor, version)

    try:
        plugin_fn.registerNode(BasicDeformerNode.TYPE_NAME, BasicDeformerNode.TYPE_ID,
                               BasicDeformerNode.creator,
                               BasicDeformerNode.initialize,
                               ommpx.MPxNode.kDeformerNode
                               )
    except:
        pass

def uninitializePlugin(plugin):

    plugin_fn = ommpx.MFnPlugin(plugin)

    try:
        plugin_fn.deregisterNode(BasicDeformerNode.TYPE_ID)
    except:
        pass