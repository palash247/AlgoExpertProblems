# with array
# def getNthFib(n):
#     # Write your code here.
# 	array = [0,1]
# #	if n<=0:
# #		return 0
# 	if n==1:
# 		return 0
# 	for i in range(2,n):
# 		array.append(array[-1]+array[-2])
# 	return array[-1]

# with cache (memoization)
cache = dict()	
def getNthFib(n):
	if n==1:
		return 0
	if n==2:
		return 1
	elif n in cache:
		return cache[n]
	cache[n] = getNthFib(n-1)+getNthFib(n-2)
	return cache[n]
