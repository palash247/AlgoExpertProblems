def kadanesAlgorithm(array):
    # Write your code here.
	_max = array[0] 
	result = [0 for x in array]
	result[0] = array[0]
	for i in range(1,len(array)):
		result[i] = max(result[i-1]+array[i],array[i])
		if _max<result[i]:
			_max = result[i]
	return _max
