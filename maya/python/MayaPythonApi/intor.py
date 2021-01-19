import maya.OpenMaya as om
mSelectionList = om.MSelectionList() #created a selection list
mSelectionList.add("pPlane1|pSphere1") #added a object from the scene and added into the selection list

mDagPath = om.MDagPath() #created a obj capable of containing the dag path of an object.
mSelectionList.getDagPath(0,mDagPath) #requested the DAG path of the obj that is on the index 0 in the selection list
print(mDagPath.fullPathName())

mObj = om.MObject() #spelisied handle.
mSelectionList.getDependNode(0,mObj) #requested the dependency node that i on the index 0 in the selection list.
print(mObj.apiTypeStr())


# selection list
mSelection = om.MSelectionList()
mSelection.add('pPlane1')

# creating MObject and MDagPath
mObj = om.MObject()
mDagPath = om.MDagPath()

# request dependency node and dag path of the object
mSelection.getDependNode(0,mObj)
mSelection.getDagPath(0,mDagPath)
