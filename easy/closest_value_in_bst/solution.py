def findClosestValueInBst(tree, target):
	closest = float('inf')
	while tree:
		if abs(tree.value-target)<abs(closest-target):
			closest = tree.value
		if tree.value >= target:
			tree = tree.left
		elif tree.value < target:
			tree = tree.right
	return closest
