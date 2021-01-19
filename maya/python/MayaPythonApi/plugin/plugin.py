import maya.OpenMaya as om
import maya.OpenMayaMPx as omMPx
import sys

commandName = "pluginCommand"


# define the plugin as a class
class pluginCommand(omMPx.MPxCommand):

    def __init__(self):
        omMPx.MPxCommand.__init__(self)

    def doIt(self, argList):
        print "doIt"


# create instance of the class
def cmdCreator():
    # attach a pointer
    return omMPx.asMPxPtr(pluginCommand())


# initialize the plugin
# maya prepare as handle as mobject
def initializePlugin(mobject):
    mplugin = omMPx.MFnPlugin(mobject)
    try:
        mplugin.registerCommand(commandName, cmdCreator)
    except:
        sys.stderr.write("Failded to register command :" + commandName)


# un-initialize the plugin
def uninitializePlugin(mobject):
    mplugin = omMPx.MFnPlugin(mobject)
    try:
        mplugin.deregisterCommand(commandName)
    except:
        sys.stderr.write("Failded to de-register command  :" + commandName)




