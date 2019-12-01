def hasSingleCycle(array):
    # Write your code here.
    result = [0 for x in array]
    n = len(array)
    i = 0
    for j in range(n):
        i=(i+array[i])%n
        result[i] += 1
        if result[i]>1:
            return False
    return sum(result)==n and i==0
