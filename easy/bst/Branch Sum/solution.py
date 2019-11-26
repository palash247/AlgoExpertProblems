# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
    result = []
	inorder_traverse(root,result,branch_sum=0)
	return result

def inorder_traverse(root,result,branch_sum=0):
	if not root:
		return
	elif root.left is None and root.right is None:
		result.append(branch_sum+root.value)
	else:
		inorder_traverse(root.left,result,branch_sum+root.value)
		inorder_traverse(root.right,result,branch_sum+root.value)
