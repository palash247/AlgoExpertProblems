def threeNumberSum(array, targetSum):
	# write your code here
	array = sorted(array) # O(nlog(n))
	result = []
	for i in range(len(array)-2):
		l = i+1
		r = len(array)-1
		while l<r:
			csum=array[i]+array[l]+array[r]
			if csum == targetSum:
				result.append([array[i],array[l],array[r]])
				l+=1
				r-=1
			elif csum < targetSum:
				l+=1
			else:
				r-=1
	return result

