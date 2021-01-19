import maya.api.OpenMaya as om


def maya_useNewAPI():
    '''
    Using maya new API 2.0
    :return:
    '''

class MultiplyNode(om.MPxNode):

    TYPE_NAME = "gMultiply"
    TYPE_ID = om.MTypeId(0x0007f7f7)

    multipliter_obj = None
    multiplicant_obj = None
    product_obj = None

    def __init__(self):
        super(MultiplyNode, self).__init__()

    def compute(self, plug, data):

        if plug == MultiplyNode.product_obj:
            multiplier = data.inputValue(MultiplyNode.multipliter_obj).asDouble()
            multiplicant = data.inputValue(MultiplyNode.multiplicant_obj).asDouble()
            product = multiplier * multiplicant

            product_data_handle = data.outputValue(MultiplyNode.product_obj)
            product_data_handle.setDouble(product)

            data.setClean(plug)


    @classmethod
    def creator(cls):
        return MultiplyNode()

    @classmethod
    def initialize(cls):
        numeric_attr = om.MFnNumericAttribute()

        #create attribute
        cls.multipliter_obj = numeric_attr.create("multiplier", "mul", om.MFnNumericData.kDouble, 2)
        numeric_attr.keyable = True #set it as keyable
        numeric_attr.readable = False # this block it to pass through

        cls.multiplicant_obj = numeric_attr.create("muliplicant", "mulC", om.MFnNumericData.kDouble, 0.0)
        numeric_attr.keyable = True #set it as keyable

        cls.product_obj = numeric_attr.create("product", "prod", om.MFnNumericData.kDouble, 0.0)
        numeric_attr.writable = False

        # add attribute
        cls.addAttribute(cls.multipliter_obj)
        cls.addAttribute(cls.multiplicant_obj)
        cls.addAttribute(cls.product_obj)

        # attribute affects
        cls.attributeAffects(cls.multipliter_obj, cls.product_obj)
        cls.attributeAffects(cls.multiplicant_obj, cls.product_obj)

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
                              MultiplyNode.creator,
                              MultiplyNode.initialize,
                              om.MPxNode.kDependNode
                              )
    except:
        om.MGlobal.displayError("Failed to register: {0}".format(MultiplyNode.TYPE_NAME))

def uninitializePlugin(plugin):

    plugin_fn = om.MFnPlugin(plugin)

    try:
       plugin_fn.deregisterNode(MultiplyNode.TYPE_ID)
    except:
        om.MGlobal.displayError("Faild to de-register: {0}".format(MultiplyNode.TYPE_NAME))
