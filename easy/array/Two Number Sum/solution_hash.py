def twoNumberSum(array, targetSum):
	_hash = dict()
	for num in array:
		if targetSum-num in _hash:
			return sorted([num,targetSum-num])
		_hash[num]=True
	return []
