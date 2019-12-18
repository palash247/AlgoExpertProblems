def groupAnagrams(words):
    # Write your code here.
    from collections import defaultdict
    result = defaultdict(list)
    for word in words:
        result["".join(sorted(word))].append(word)
    return [result[x] for x in result]
