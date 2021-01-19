import maya.OpenMaya as om
import maya.OpenMayaMPx as ommpx
import maya.cmds as mc

class BlendDeformerNode(ommpx.MPxDeformerNode):

    TYPE_NAME = "BlendDeformerNode"
    TYPE_ID = om.MTypeId(0x0008f8fC)

    def __init__(self):
        super(BlendDeformerNode, self).__init__()

    def deform(self, data_block, geo_iter, matrix, multi_index):
        '''
        :param data_block: This is MDatablock Object, this provides access to nodes attribute values
        :param geo_iter: MIt, iterator.
        :param matrix: MMatrix, world transform matrix.
        :param multi_index: integer, ex: geometry with multiple components.
        :return:
        '''
        envelope = data_block.inputValue(self.envelope).asFloat()
        if envelope == 0:
            return

        blend_weight = data_block.inputValue(BlendDeformerNode.blend_weight).asFloat()
        if blend_weight == 0:
            return
        target_mesh = data_block.inputValue(BlendDeformerNode.blend_mesh).asMesh()
        if target_mesh.isNull():
            return

        target_points = om.MPointArray()
        target_mesh_fn = om.MFnMesh(target_mesh)
        target_mesh_fn.getPoints(target_points)

        global_weight = blend_weight * envelope

        geo_iter.reset()
        while not geo_iter.isDone():


            source_pt = geo_iter.position()
            target_pt = target_points[geo_iter.index()]

            source_weight = self.weightValue(data_block, multi_index, geo_iter.index())

            final_pt = (source_pt + (target_pt - source_pt) * global_weight * source_weight)

            geo_iter.setPosition(final_pt)



            geo_iter.next()

    @classmethod
    def creator(cls):
        return BlendDeformerNode()

    @classmethod
    def initialize(cls):

        typed_attr = om.MFnTypedAttribute()
        cls.blend_mesh = typed_attr.create("BlendMesh", "bMesh", om.MFnData.kMesh)

        numric_attr = om.MFnNumericAttribute()
        cls.blend_weight = numric_attr.create("blendWight", "bWeight", om.MFnNumericData.kFloat, 0.0)
        numric_attr.setKeyable(True)
        numric_attr.setMin(0.0)
        numric_attr.setMax(1.0)

        cls.addAttribute(cls.blend_mesh)
        cls.addAttribute(cls.blend_weight)

        output_geom = ommpx.cvar.MPxGeometryFilter_outputGeom

        cls.attributeAffects(cls.blend_mesh, output_geom)
        cls.attributeAffects(cls.blend_weight, output_geom)




def initializePlugin(plugin):

    vendor = "Deepak Rajan"
    version = "1.0.0"

    plugin_fn = ommpx.MFnPlugin(plugin, vendor, version)

    try:
        plugin_fn.registerNode(BlendDeformerNode.TYPE_NAME, BlendDeformerNode.TYPE_ID,
                               BlendDeformerNode.creator,
                               BlendDeformerNode.initialize,
                               ommpx.MPxNode.kDeformerNode
                               )
    except:
        pass

    #make it paintable
    mc.makePaintable(BlendDeformerNode.TYPE_NAME, "weights", attrType = "multiFloat", shapeMode = "deformer")

def uninitializePlugin(plugin):
    mc.makePaintable(BlendDeformerNode.TYPE_NAME, "weights",remove = True)

    plugin_fn = ommpx.MFnPlugin(plugin)

    try:
        plugin_fn.deregisterNode(BlendDeformerNode.TYPE_ID)
    except:
        pass