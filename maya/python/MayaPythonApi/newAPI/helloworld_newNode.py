'''
Extending maya with new locator node and draw override with viewport 2.0
'''

import maya.api.OpenMaya as om
import maya.api.OpenMayaRender as omr
import maya.api.OpenMayaUI as omUI
import maya.cmds as mc
import sys


# this function indicates maya that the api used is 2.0
def maya_useNewAPI():
    pass
# TODO this has to be return

class HelloWorldNode(omUI.MPxLocatorNode):

    TYPE_NAME = "helloworld"
    TYPE_ID = om.MTypeId(0x0007f7f7)
    DRAW_CLASSIFICATION = "drawdb/geomentry/helloworld"
    DRAW_REGISTRANT_ID = "HelloWorldNode"

    def __init__(self):
        super(HelloWorldNode, self).__init__()

    @classmethod
    def creator(cls):
        return HelloWorldNode()

    @classmethod
    def initialize(cls):
        pass


class HelloWroldDrawOverride(omr.MPxDrawOverride):

    NAME = "HelloWorldDrawOverride"

    def __init__(self, obj):
        super(HelloWroldDrawOverride, self).__init__(obj, None, False)

    def prepareForDraw(self, obj_path, camera_path, frame_context, old_data):
        pass

    def supportedDrawAPIs(self):
        return omr.MRenderer.kAllDevices

    def hasUIDrawables(self):
        return True

    def addUIDrawables(self, obj_path, draw_manager,frame_context,data):
        draw_manager.beginDrawable()
        draw_manager.text2d(om.MPoint(100,100), "Hello World")
        draw_manager.endDrawable()

    @classmethod
    def creator(cls, obj):
       return HelloWroldDrawOverride(obj)

# plugin intialize and un-initialize -------------

def initializePlugin(plugin):  # parameter is mobject - plugin

    vendor = "Grey - RnD plugin - Dev - Deepak Rajan"
    version = "1.0.0"

    plugin_fn = om.MFnPlugin(plugin, vendor, version)
    try:
        plugin_fn.registerNode(HelloWorldNode.TYPE_NAME,
                               HelloWorldNode.TYPE_ID,
                               HelloWorldNode.creator,
                               HelloWorldNode.initialize,
                               om.MPxNode.kLocatorNode,
                               HelloWorldNode.DRAW_CLASSIFICATION)
    except:
        om.MGlobal.displayError("Failed to rigister Node: {0}".format(HelloWorldNode.TYPE_NAME))

    try:
        omr.MDrawRegistry.registerDrawOverrideCreator(HelloWorldNode.DRAW_CLASSIFICATION,
                                                      HelloWorldNode.DRAW_REGISTRANT_ID,
                                                      HelloWroldDrawOverride.creator)

    except:
       pass


def uninitializePlugin(plugin):

    plugin_fn= om.MFnPlugin(plugin)
    try:
        omr.MDrawRegistry.deregisterDrawOverrideCreator(HelloWorldNode.DRAW_CLASSIFICATION,HelloWorldNode.DRAW_REGISTRANT_ID)

    except:
        pass
    try:
        plugin_fn.deregisterNode(HelloWorldNode.TYPE_ID)
    except:
        om.MGlobal.displayError("Failed to de-rigister Node: {0}".format(HelloWorldNode.TYPE_NAME))