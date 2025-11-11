def isValid(s) -> bool:
    stackk = []
    for item in s:
        if item in ["(", "{", "["]:
            stackk.append(item)
            # print(stackk)

        elif item in [")", "}", "]"] and len(stackk) > 0:
            top_element = stackk[len(stackk) - 1]

            if item == ")" and top_element == "(":
                stackk.pop()
                # print(stackk)
            elif item == "}" and top_element == "{":
                stackk.pop()
                # print(stackk)
            elif item == "]" and top_element == "[":
                stackk.pop()
                # print(stackk)
            else:
                return False
        else:
            return False
    if not stackk:
        return True
    else:
        return False


print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("([])"))
print(isValid("([)]"))
