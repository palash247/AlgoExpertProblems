def powerset(array):
    result = [[]]
    for each in array:
        temp = result[:]
        for sub_set in temp:
            result.append(sub_set + [each])
    return result


if '__main__' == __name__:
    result = powerset([1, 2, 3])
    print(result)
