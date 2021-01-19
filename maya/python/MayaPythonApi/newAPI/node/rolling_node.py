import maya.api.OpenMaya as om
import maya.cmds as mc

def maya_useNewAPI():
    '''
    Using maya new API 2.0
    :return:
    '''

class RollingNode(om.MPxNode):

    TYPE_NAME = "gRolling"
    TYPE_ID = om.MTypeId(0x0007f9f9)

    distance_obj = None
    radius_obj = None
    rotation_obj = None

    def __init__(self):
        super(RollingNode, self).__init__()

    def compute(self, plug, data):
        if plug == self.rotation_obj:

            distance = data.inputValue(RollingNode.distance_obj).asDouble()
            radius = data.inputValue(RollingNode.radius_obj).asDouble()

            if radius == 0:
                rotation = 0
            else:
                rotation = (distance / radius) * -1
            #set rotation value
            rotation_data_handle = data.outputValue(RollingNode.rotation_obj)
            rotation_data_handle.setDouble(rotation)

            #mark the plug clean
            data.setClean(plug)

    @classmethod
    def creator(cls):
        return RollingNode()

    @classmethod
    def initialize(cls):
        numeric_attr = om.MFnNumericAttribute()

        cls.distance_obj = numeric_attr.create("distance", "dist", om.MFnNumericData.kDouble, 0.0)
        numeric_attr.keyable = True

        cls.radius_obj = numeric_attr.create("radius", "rad", om.MFnNumericData.kDouble, 0.0)
        numeric_attr.keyable = True

        unit_attr = om.MFnUnitAttribute()
        cls.rotation_obj = unit_attr.create("rotation", "rot", om.MFnUnitAttribute.kAngle, 0.0)

        #add attribute
        cls.addAttribute(cls.distance_obj)
        cls.addAttribute(cls.radius_obj)
        cls.addAttribute(cls.rotation_obj)

        cls.attributeAffects(cls.distance_obj, cls.rotation_obj)
        cls.attributeAffects(cls.radius_obj, cls.rotation_obj)

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
       plugin_fn.registerNode(RollingNode.TYPE_NAME, RollingNode.TYPE_ID,
                              RollingNode.creator, #functin/method that returns new instance of class
                              RollingNode.initialize, # function/method that will initialize all attributes of node
                              om.MPxNode.kDependNode # type of node to be registered.
                              )
    except:
        om.MGlobal.displayError("Failed to register: {0}".format(RollingNode.TYPE_NAME))

def uninitializePlugin(plugin):

    plugin_fn = om.MFnPlugin(plugin)

    try:
       plugin_fn.deregisterNode(RollingNode.TYPE_ID)
    except:
        om.MGlobal.displayError("Faild to de-register: {0}".format(RollingNode.TYPE_NAME))