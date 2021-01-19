import maya.OpenMaya as om
# selection list
mSelection = om.MSelectionList()
mSelection.add('pPlane1')

# creating MObject and MDagPath
mObj = om.MObject()
mDagPath = om.MDagPath()

# request dependency node and dag path of the object
mSelection.getDependNode(0,mObj)
mSelection.getDagPath(0,mDagPath)

# mesh function set
mFnMesh = om.MFnMesh(mDagPath)
mFnMesh.fullPathName()

# dependency node function set
mFnDependNode = om.MFnDependencyNode(mObj)
mFnDependNode.name()

# get all the connections of a shape node.
mPlugArray = om.MPlugArray()
mFnMesh.getConnections(mPlugArray)

mPlugArray.length()
print mPlugArray[0].name()
print mPlugArray[1].name()

mPlugArray_connections = om.MPlugArray()
mPlugArray[1].connectedTo(mPlugArray_connections, True, False)
mPlugArray_connections.length()

print mPlugArray_connections[0].name()


mObj2 = mPlugArray_connections[0].node()

mFnDependNode2 = om.MFnDependencyNode(mObj2)
print mFnDependNode2.name()

# get values of the attributes from the node.
mPlug_width = mFnDependNode2.findPlug("width")
mPlug_height = mFnDependNode2.findPlug("height")
print mPlug_width.asFloat()
print mPlug_height.asInt()

mPlug_subW = mFnDependNode2.findPlug("subdivisionsWidth")
mPlug_subH = mFnDependNode2.findPlug("subdivisionsHeight")
print mPlug_subW.asFloat()
print mPlug_subH.asInt()

#set value of the node.
mPlug_subW.setFloat(10.0)
mPlug_subH.setInt(10)


