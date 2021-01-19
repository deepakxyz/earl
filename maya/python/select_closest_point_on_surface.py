# select the closest point on surface

import maya.OpenMaya as OpenMaya
from pymel.core import *

geo = PyNode('pSphere1')
pos = PyNode('locator1').getRotatePivot(space='world')

nodeDagPath = OpenMaya.MObject()
try:
    selectionList = OpenMaya.MSelectionList()
    selectionList.add(geo.name())
    nodeDagPath = OpenMaya.MDagPath()
    selectionList.getDagPath(0, nodeDagPath)
except:
    warning('OpenMaya.MDagPath() failed on %s' % geo.name())

mfnMesh = OpenMaya.MFnMesh(nodeDagPath)

pointA = OpenMaya.MPoint(pos.x, pos.y, pos.z)
pointB = OpenMaya.MPoint()
space = OpenMaya.MSpace.kWorld

util = OpenMaya.MScriptUtil()
util.createFromInt(0)
idPointer = util.asIntPtr()

mfnMesh.getClosestPoint(pointA, pointB, space, idPointer)  
idx = OpenMaya.MScriptUtil(idPointer).asInt()

faceVerts = [geo.vtx[i] for i in geo.f[idx].getVertices()]
closestVertex = None
minLength = None
for v in faceVerts:
    thisLength = (pos - v.getPosition(space='world')).length()
    if minLength is None or thisLength < minLength:
        minLength = thisLength
        closestVertex = v
select(closestVertex)