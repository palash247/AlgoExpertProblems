def get_permutations(array):
    permutations = []
    gen_permutations(array, [], permutations)
    return permutations

def gen_permutations(array, current_permutation, permutations):
    if not array and current_permutation:
        return permutations.append(current_permutation)
    else:
        for i,_ in enumerate(array):
            rest_array = array[:i] + array[i+1:]
            new_permutation = current_permutation + [array[i]]
            gen_permutations(rest_array, new_permutation, permutations)
