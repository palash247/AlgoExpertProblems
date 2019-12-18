def balancedBrackets(string):
    # Write your code here.
    opening = ["(", "[", "{"]
    closing = {"}":"{", ")":"(", "]":"["}
    
    stack = []
    for each in string:
        if each in opening:
            stack.append(each)
        elif each in closing:
            if not stack:
                return False
            elif stack[-1]==closing[each]:
                stack.pop()
            else:
                return False
            
    if len(stack)==0:
        return True
    else:
        return False
