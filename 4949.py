while True:
    s = input()
    stack = []

    if s ==".":
        break

    for j in s:
        if j == "(" or j == "[":
            stack.append(j)
        elif j == ")":
            if len(stack) != 0 and stack[-1] =="(":
                stack.pop()
            else:
                stack.append(")")
                break
        elif j == "]":
            if len(stack) != 0 and stack[-1] == "[":
                stack.pop()
            else:
                stack.append("]")
                break
    
    if len(stack) == 0:
        print("yes")
    else:
        print("no")
