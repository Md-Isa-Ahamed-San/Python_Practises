
def minLengthAfterRemovals(s):
    stack =[]

    for char in s:
        if not stack:
            stack.append(char)
        else:
            top_element = stack[-1]
            if (char == 'b' and top_element == 'a') or (char == 'a' and top_element == 'b'):
                stack.pop()
            else:
                stack.append(char)
    return len(stack)

minLengthAfterRemovals("abccba")


