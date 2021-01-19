import maya.api.OpenMaya as om

# get attribute value of the selection

node_name = "pCube1"
attribute_name = "translateY"

selection_list = om.MSelectionList()
selection_list.add(node_name)

obj = selection_list.getDependNode(0)

if obj.hasFn(om.MFn.kTransform):
    transfrom_fn = om.MFnTransform(obj)

    plug = transfrom_fn.findPlug(attribute_name, False)

    attribute_value = plug.asDouble()
    print("{0}: {1}".format(plug, attribute_value))

    plug.setDouble(20.0)  # set value to the attribute.

# ______________________________________________________________
# get attribute of the child objects

import maya.api.OpenMaya as om

node_name = "pCube1"
attribute_name = "translate"

selection_list = om.MSelectionList()
selection_list.add(node_name)

obj = selection_list.getDependNode(0)

if obj.hasFn(om.MFn.kTransform):
    transfrom_fn = om.MFnTransform(obj)

    plug = transfrom_fn.findPlug(attribute_name, False)

    if plug.isCompound:
        for i in range(plug.numChildren()):
            child_plug = plug.child(i)

            attribute_value = child_plug.asDouble()
            print("{0}: {1}".format(child_plug, attribute_value))


