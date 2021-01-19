from Katana import KatanaFile, NodegraphAPI 
from proceduralShading import psn_procedural


def procd(nodeName = 'Hammer'):
    prod.replace('Hammer',nodeName)
    root = NodegraphAPI.GetRootNode()
    KatanaFile.Paste( prod, root )

procd(nodeName = 'chetos')