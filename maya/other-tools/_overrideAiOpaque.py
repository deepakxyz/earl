import maya.cmds as mc
import maya.OpenMaya as om

class arnoldOpaqueOverride(object):
    '''
    Class for overriding arnold Opaque State
    '''
    
    @classmethod
    def overrideaiOpaque(cls, booleann):
        if (booleann < 0 or booleann > 1):
            om.MGlobal.displayError("Not a Boolean Value")
            return False
            
        shapes = cls.shapeNodes_Selection()
        if not shapes:
            om.MGlobal.displayError("No shapeNode selected")
            
        for shape in shapes:
            mc.setAttr("{0}.aiOpaque".format(shape), booleann)
            
            
        return True
    
    @classmethod
    def shapeNodes_Selection(cls):
        selection = mc.ls(selection = True)
        if not selection:
            return None

        shapes=[]
        for node in selection:
            shapes.extend(mc.listRelatives(node, shapes = True))
            
        return shapes
        