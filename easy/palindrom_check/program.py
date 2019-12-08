def isPalindrome(string):
    # Write your code here.
	n = len(string)
	half = n//2
	i=0
	j=n-1
	while i<half and j>=half:
		if string[i]!=string[j]:
			return False
		i+=1
		j-=1
	return True
