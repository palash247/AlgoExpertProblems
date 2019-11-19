def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
    results = [0 for x in range(n+1)]
	results[0] = 1
	for denom in denoms:
		for i in range(denom,n+1):
			if i >= denom:
				results[i] += results[i-denom]
	return results[-1]
