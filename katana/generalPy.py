from Katana import NodegraphAPI

lightMaterialNode = NodegraphAPI.CreateNode('Material', NodegraphAPI.GetRootNode())
NodegraphAPI.SetNodePosition(lightMaterialNode, (500, 400))
lightMaterialNode.getParameter('name').setValue('spotLight_shader', 0)
lightMaterialNode.getParameter('namespace').setValue('lgt', 0)
lightMaterialNode.addShaderType('prmanLight')
lightMaterialNode.checkDynamicParameters()
lightMaterialNode.getParameter('shaders.prmanLightShader.enable').setValue(1, 0)
lightMaterialNode.getParameter('shaders.prmanLightShader.value').setValue('PxrRectLight', 0)
lightMaterialNode.checkDynamicParameters()





networkMaterialNode.getInputPort('arnoldSurface').connect(
    standardNode.getOutputPort('out'))