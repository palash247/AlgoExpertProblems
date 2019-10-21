def twoNumberSum(array, targetSum):
	array = sorted(array)
	l = 0
	r = len(array)-1
	while(l<r):
		total = array[l]+array[r]
		if total == targetSum:
			return [array[l],array[r]]
		elif total < targetSum:
			l+=1
		elif total > targetSum:
			r-=1
	return []
