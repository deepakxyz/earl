import maya.OpenMaya as om
import maya.OpenMayaMPx as omMPx
import sys
import math

nodeName = "RippleDeformer"
nodeId = om.MTypeId(0x102fff)


class Ripple(omMPx.MPxDeformerNode):
    '''
    Commands ---> MPxCommand
    Custome ----> MPxNode
    Deformer ---> MPxDeformerNode
    '''

    mObj_amplitude = om.MObject()
    mObj_displace = om.MObject()

    def __init__(self):
        omMPx.MPxDeformerNode.__init__(self)

    def deform(self, dataBlock, geoIterator, matrix, geometryIndex):

        input = omMPx.cvar.MPxDeformerNode_input
        # 1. Attach a handel to input Array Attribute.
        dataHandelInputArray = dataBlock.inputArrayValue(input)
        # 2. Jump to particular Element
        dataHandelInputArray.jumpToElement(geometryIndex)
        # 3. Attach a handel to specific data block
        dataHandelInputElement = dataHandelInputArray.inputValue()
        # 4. Reach to the child - inputGeom

        inputGeom = omMPx.cvar.MPxDeformerNode_inputGeom
        dataHandelInputGeom = dataHandelInputElement.child(inputGeom)
        inMesh = dataHandelInputGeom.asMesh()

        # envelope
        envelope = omMPx.cvar.MPxDeformerNode_envelope
        dataHandelEnvelope = dataBlock.inputValue(envelope)
        envelopeValue = dataHandelEnvelope.asFloat()

        # amplitude
        dataHandelAmplitude = dataBlock.inputValue(Ripple.mObj_amplitude)
        amplitudeValue = dataHandelAmplitude.asFloat()

        # displace
        dataHandelDisplace = dataBlock.inputValue(Ripple.mObj_displace)
        displaceValue = dataHandelDisplace.asFloat()

        mFloatVectorArray_normal = om.MFloatVectorArray()
        mFnMesh = om.MFnMesh(inMesh)
        mFnMesh.getVertexNormals(False, mFloatVectorArray_normal, om.MSpcae.kObject)

        while (not geoIterator.isDone()):
            pointPosition = geoIterator.poisition()

            pointPosition.x = pointPosition.x + math.sin(geoIterator.index() + displaceValue) * amplitudeValue * \
                              mFloatVectorArray_normal[geoIterator.index()].x * envelopeValue
            pointPosition.y = pointPosition.y + math.sin(geoIterator.index() + displaceValue) * amplitudeValue * \
                              mFloatVectorArray_normal[geoIterator.index()].y * envelopeValue
            pointPosition.z = pointPosition.z + math.sin(geoIterator.index() + displaceValue) * amplitudeValue * \
                              mFloatVectorArray_normal[geoIterator.index()].z * envelopeValue

            geoIterator.setPosition(pointPosition)
            geoIterator.next()


def deformerCreator():
    nodePointer = omMPx.asMPxPtr(Ripple())
    return nodePointer


def nodeInitializer():
    '''
    create Attributes
    Attrach Attributes to the node
    Design Circuitry
    '''

    mFnAttr = om.MFnNumericAttribute()
    Ripple.mObj_amplitude = mFnAttr.create("AmplitudeValue", "AttrVal", om.MFnNumericData.kFloat, 0.0)
    mFnAttr.setKeyable(1)
    mFnAttr.setMin(0.0)
    mFnAttr.setMax(1.0)

    Ripple.mObj_displace = mFnAttr.create("DisplaceValue", "DispVal", om.MFnNumericData.kFloat, 0.0)
    mFnAttr.setKeyable(1)
    mFnAttr.setMin(0.0)
    mFnAttr.setMax(10.0)

    Ripple.addAttribute(Ripple.mObj_amplitude)
    Ripple.addAttribute(Ripple.mObj_displace)

    '''
    SWIG - simplified Wrapper Interface Generator
    '''

    outputGeom = omMPx.cvar.MPxDeformerNode_outputGeom
    Ripple.attributeAffects(Ripple.mObj_amplitude, outputGeom)
    Ripple.attributeAffects(Ripple.mObj_displace, outputGeom)


def initializePlugin(mobject):
    mplugin = omMPx.MFnPlugin(mobject)
    try:
        mplugin.registerNode(nodeName, nodeId, deformerCreator, nodeInitializer, omMPx.MPxNode.kDeformerNode)
    except:
        sys.stderr.write("Failed to register node: %s" % nodeName)
        raise


def uninitializePlugin(mobject):
    mplugin = omMPx.MFnPlugin(mobject)
    try:
        mplugin.deregisterNode(nodeId)
    except:
        sys.stderr.write("Failed to register node: %s" % nodeName)
        raise
