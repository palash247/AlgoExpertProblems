def selectionSort(array):
    # Write your code here.
	min = float('inf')
	for i in range(len(array)):
		min = array[i]
		indx = i
		for j in range(i,len(array)):
			if min>array[j] and i!=j:
				min = array[j]
				indx = j
		if i!=j:
			swap(i,indx,array)
	return array

def swap(i,indx,array):
	array[i],array[indx] = array[indx],array[i]
