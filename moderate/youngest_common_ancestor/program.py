# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

# before seeing the solution
# def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
#     # Write your code here.
#     desc1_path = get_ancestor_path(descendantOne)
#     desc2_path = get_ancestor_path(descendantTwo)
#     i = 0
#     while i<len(desc1_path) and i<len(desc2_path):
#         if desc1_path[i].name == desc2_path[i].name:
#             i += 1
#         else:
#             break
#     return desc1_path[i-1]

# def get_ancestor_path(node):
#     path = []
#     while node:
#         path.insert(0,node)
#         node = node.ancestor
#     return path

# after seeing the solution
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    desc1_depth = get_ancestor_depth(descendantOne)
    desc2_depth = get_ancestor_depth(descendantTwo)
    
    if desc1_depth<desc2_depth:
        return parse_depth_wise(descendantOne, descendantTwo, desc2_depth-desc1_depth)
    else:
        return parse_depth_wise(descendantTwo, descendantOne, desc1_depth - desc2_depth)

def get_ancestor_depth(node):
    depth = 0
    while node:
        node = node.ancestor
        depth += 1
    return depth

def parse_depth_wise(old_node, young_node, diff):
    while diff>0:
        young_node = young_node.ancestor
        diff-=1
    while young_node.name != old_node.name:
        young_node = young_node.ancestor
        old_node = old_node.ancestor
    return young_node
