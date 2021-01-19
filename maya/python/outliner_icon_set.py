from maya import cmds, OpenMaya as om

node = cmds.createNode("joint")
sel = om.MSelectionList()
mobj = om.MObject()
om.MGlobal.getActiveSelectionList(sel)
sel.getDependNode(0, mobj)
fn = om.MFnDependencyNode(mobj)
fn.setIcon("Y:/codeBlock/maIcons/rand.png")