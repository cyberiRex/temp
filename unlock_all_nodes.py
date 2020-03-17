# Lock

import maya.cmds as cmds

all_nodes = cmds.ls()
locked_nodes = list()

for a in all_nodes:
   if cmds.lockNode(a, l=True, q=True)[0]:
    locked_nodes.append(a)

print locked_nodes
