from Katana import NodegraphAPI

def networkMaterial(materialName):

    psnNodeName = 'psn_'+ materialName
    psnNode = NodegraphAPI.CreateNode('PrmanShadingNode', NodegraphAPI.GetRootNode())
    NodegraphAPI.SetNodePosition(psnNode, (500, 400))
    psnNode.getParameter('name').setValue(psnNodeName, 0.0)
    psnNode.getParameter('nodeType').setValue('PxrSurface', 0.0)
    psnNode.checkDynamicParameters()

    netWorkMaterial = NodegraphAPI.CreateNode('NetworkMaterial', NodegraphAPI.GetRootNode())
    NodegraphAPI.SetNodePosition(netWorkMaterial, (500, 350))
    netWorkMaterial.getParameter('name').setValue(materialName, 0)
    netWorkMaterial.addInputPort('prmanBxdf')

    netWorkMaterial.getInputPort('prmanBxdf').connect(psnNode.getOutputPort('out'))

def pxrTexture(textureName):
    diffuse = 'tex_diffuse_' + textureName
    psnNode = NodegraphAPI.CreateNode('PrmanShadingNode', NodegraphAPI.GetRootNode())
    NodegraphAPI.SetNodePosition(psnNode, (200, 350))
    psnNode.getParameter('name').setValue(diffuse, 0.0)
    psnNode.getParameter('nodeType').setValue('PxrTexture', 0.0)
    psnNode.checkDynamicParameters()

    specular = 'tex_specular_' + textureName
    psnNode1 = NodegraphAPI.CreateNode('PrmanShadingNode', NodegraphAPI.GetRootNode())
    NodegraphAPI.SetNodePosition(psnNode1, (200, 400))
    psnNode1.getParameter('name').setValue(specular, 0.0)
    psnNode1.getParameter('nodeType').setValue('PxrTexture', 0.0)
    psnNode1.checkDynamicParameters()

def printFun(test):
    print(test)