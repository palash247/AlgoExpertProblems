def moveElementToEnd(array, toMove):
    # Write your code here.
    left = 0
	right = len(array)-1
	while left<right:
		if array[left]!=toMove:
			left+=1
		if array[right]==toMove:
			right-=1
		if array[left]==toMove and array[right]!=toMove:
			swap(array,left,right)
	return array

def swap(array,left,right):
	array[left],array[right]=array[right],array[left]

