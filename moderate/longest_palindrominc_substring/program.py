def get_longest_palindromic_substring(string):
    current_longest = [0, 1]
    # check for odd length palindromic substring
    for i in range(len(string)):
        odd = check_longest_palindrom(string, i-1, i+1)
        even = check_longest_palindrom(string, i-1, i)
        current_longest = max(odd, even, current_longest, key = lambda x: x[1]-x[0])
    return string[current_longest[0]:current_longest[1]]

def check_longest_palindrom(string, left, right):
    while left >= 0 and right < len(string):
        if string[left] == string[right]:
            left -= 1
            right += 1
        else:
            break
    return [left+1, right]

if __name__=='__main__':
    print("Input")
    print("acaxyzzyx")
    print("Output")
    print(get_longest_palindromic_substring("acaxyzzyx"))
