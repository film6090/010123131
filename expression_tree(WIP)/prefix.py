def pretree(string):
    rout = []
    out = []
    stack = []
    c = 0
    p1 = False
    ct=0
    for i in range(len(string)):
        if string[i] == ')':
            rout.append(stack.pop())
            c=0
        elif string[i] == '!':
            if string[i+1] == 'I' or string[i+1] == '|':
                h = string[i:i+3]
                rout.append(h)
                c += 1
                p1 = True
                if c == 2:
                    c=0
                    rout.append(stack.pop())
            else:
                stack.append(string[i])
        elif any(x in string[i] for x in op):
            stack.append(string[i])
        elif string[i] == '|' or string[i] == 'I':
            if p1 == False:
                h = string[i:i+2]
                rout.append(h)
                c+=1
                if c == 2:
                    c = 0
                    rout.append(stack.pop())
            else:
                p1=False
    while len(stack) != 0:
        rout.append(stack.pop())
    while len(rout) != 0:
        out.append(rout.pop())
    return out
