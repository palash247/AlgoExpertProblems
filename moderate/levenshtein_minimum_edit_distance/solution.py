def levenshteinDistance(str1, str2):
    # Write your code here.
    result = [[0 for x in range(len(str2)+1)] for y in range(len(str1)+1)]
	for i in range(len(str1)+1):
		result[i][0] = i
	for i in range(len(str2)+1):
		result[0][i] = i
	for i in range(1,len(str1)+1):
		for j in range(1,len(str2)+1):
			if str1[i-1]!=str2[j-1]:
				result[i][j] = 1+min(result[i-1][j],result[i][j-1],result[i-1][j-1])
			else:
				result[i][j] = result[i-1][j-1]
	return result[-1][-1]
