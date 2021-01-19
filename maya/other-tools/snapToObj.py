import maya.cmds as mc
selection=mc.ls(sl=True)
snapTo = selection[0]

if mc.objExists(snapTo):
    for obj in selection[1:]:
        mc.delete(mc.pointConstraint(snapTo, obj))
        mc.delete(mc.orientConstraint(snapTo, obj))
        
else:
    print('Not enough object selected')