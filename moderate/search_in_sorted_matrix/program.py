def searchInSortedMatrix(matrix, target):
    # Write your code here.
    i = 0
    j = len(matrix[0]) -1
    while i < len(matrix) and j >= 0:
        if matrix[i][j]==target:
            return [i,j]
        if matrix[i][j]<target:
            i += 1
        if matrix[i][j]>target:
            j -= 1
    return [-1,-1]
