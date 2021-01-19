import maya.OpenMaya as om
import maya.OpenMayaMPx as ommpx

class AttractDeformerNode(ommpx.MPxDeformerNode):

    TYPE_NAME = "AttractDeformerNode"
    TYPE_ID = om.MTypeId(0x0007e7eC)

    MAX_ANGLE = 3

    def __init__(self):
        super(AttractDeformerNode, self).__init__()

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

        max_distance = data_block.inputValue(AttractDeformerNode.max_distance).asFloat()
        if max_distance == 0:
            return

        target_position = data_block.inputValue(AttractDeformerNode.target_position).asFloatVector()


        # To access mesh normals
        input_handle = data_block.outputArrayValue(self.input) #self.input : builtin attribute
        input_handle.jumpToElement(multi_index)
        input_element_handle = input_handle.outputValue()

        input_geom = input_element_handle.child(self.inputGeom).asMesh() #self.inputGeom : builtin attribute
        mesh_fn  = om.MFnMesh(input_geom)

        normals = om.MFloatVectorArray()
        mesh_fn.getVertexNormals(False, normals) # False: does not give angle weighted normals, it give you only sorround face normals

        inverse_world_matrix = matrix.inverse()

        geo_iter.reset()
        while not geo_iter.isDone():

            pt_local = geo_iter.position()
            pt_world = pt_local * matrix

            target_vector  = target_position - om.MFloatVector(pt_world)

            distance = target_vector.length()
            if distance <= max_distance:

                normal = om.MVector(normals[geo_iter.index()]) * matrix
                normal = om.MFloatVector(normal) # converting MVector to MFloatVector

                angle = normal.angle(target_vector)
                if angle <= AttractDeformerNode.MAX_ANGLE:

                    offset = target_vector * ((max_distance - distance)/ max_distance)

                    new_pt_world = pt_world + om.MVector(offset)
                    new_pt_local = new_pt_world * inverse_world_matrix

                    geo_iter.setPosition(new_pt_local)

            geo_iter.next()


    @classmethod
    def creator(cls):
        return AttractDeformerNode()

    @classmethod
    def initialize(cls):
        numeric_attr = om.MFnNumericAttribute()

        cls.max_distance = numeric_attr.create("maximumDistance", "maxDist", om.MFnNumericData.kFloat, 1.0)
        numeric_attr.setKeyable(True)
        numeric_attr.setMin(0.0)
        numeric_attr.setMax(2.0)

        cls.target_position = numeric_attr.createPoint("targetPosition", "targPos")
        numeric_attr.setKeyable(True)


        cls.addAttribute(cls.max_distance)
        cls.addAttribute(cls.target_position)

        output_geom = ommpx.cvar.MPxGeometryFilter_outputGeom
        cls.attributeAffects(cls.max_distance, output_geom)
        cls.attributeAffects(cls.target_position, output_geom)





def initializePlugin(plugin):

    vendor = "Deepak Rajan"
    version = "1.0.0"

    plugin_fn = ommpx.MFnPlugin(plugin, vendor, version)

    try:
        plugin_fn.registerNode(AttractDeformerNode.TYPE_NAME, AttractDeformerNode.TYPE_ID,
                               AttractDeformerNode.creator,
                               AttractDeformerNode.initialize,
                               ommpx.MPxNode.kDeformerNode
                               )
    except:
        pass

def uninitializePlugin(plugin):

    plugin_fn = ommpx.MFnPlugin(plugin)

    try:
        plugin_fn.deregisterNode(AttractDeformerNode.TYPE_ID)
    except:
        pass

