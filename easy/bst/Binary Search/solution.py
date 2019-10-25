def binarySearch(array, target):
    # Write your code here.
	l = 0
	b = len(array)
	
	while(l<=b):
		mid = (l+b)//2
		if array[mid]==target:
			return mid
		if target>array[mid]:
			l = mid+1
		else:
			b = mid-1
			
	return -1
		
		
