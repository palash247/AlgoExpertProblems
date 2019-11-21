def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
	arrayOne.sort()
	arrayTwo.sort()
	i = 0
	j = 0
	min = float('inf')
	result = []
	while i<len(arrayOne) and j<len(arrayTwo):
		distance = arrayOne[i]-arrayTwo[j]
		if abs(distance)<min:
				min = abs(distance)
				result = [arrayOne[i],arrayTwo[j]]
		if distance == 0:
			return [arrayOne[i],arrayOne[i]]
		elif distance<0:
			i+=1
		else:
			j+=1
	return result
