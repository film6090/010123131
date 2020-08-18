f = open(r'c:\Users\Firn_Film\Desktop\film\.vscode\text.txt','r')
t = f.readlines()
for i in range(len(t)):
    if i != len(t)-1:
        t[i] = t[i][4:len(t[i])-2]
    else:
        t[i] = t[i][4:len(t[i])-1]


def count_var(t):
    h0 = []
    var = ('|','I')
    for i in range(len(t)):
        h1 = []
        string = t[i]
        for j in range(t[i].count('|')+t[i].count('I')):
            pos0 = 99
            for x in var:
                pos1 = string.find(x)
                if pos1 != (-1):
                    if pos0 > pos1:
                        pos0 = pos1
            if not(string[pos0:pos0+2] in h1):
                h1.append(string[pos0:pos0+2])
            string = string[pos0+1:]
        h0.append(h1)
    return h0

def eq(t,h):
    y = []
    for i in range(len(t)):
        y1 = []
        if len(h[i]) != 0: 
            c = 0
            hold = t[i]
            for j in range(2**len(h[i])):
                s = "{0:b}".format(c).zfill(len(h[i]))
                for k in range(len(s)):
                    while h[i][k] in hold:
                        pos = hold.find(h[i][k])
                        hold = hold[:pos] + s[k] + hold[pos+2:]
                y1.append(hold)
                hold = t[i]
                c += 1
        else:
            y1.append(t[i])
            y.append(y1)
            y1 = []
        if y1 != []:
            y.append(y1)
    return y

def count(eq_str,start,last):
    c = 0
    st = False
    for i in range(last):
        if eq_str[start+i] == '(':
            c += 1
            st = True
        elif eq_str[start+i] == ')':
            c -= 1
        if c == 0 and st == True:
            return start+i

def bracket(s):
    pos = s.find('(')
    c = count(s,pos,len(s))
    return s[:pos] + calculate(s[pos+1:c]) + s[c+1:]

def calculate(s):
    op = ['!','&','+']
    if len(s) == 1:
        return (s)
    if '(' in s:
        pos = s.find('(')
        c = count(s,pos,len(s))
        return s[:pos] + calculate(s[pos+1:c]) + s[c+1:]
    while any( x in s for x in op):
        for t in op:    
            pos = s.rfind(t)
            if pos != -1:
                break
        if s[pos] == '+':
            if s[pos-1] == '0' and s[pos+1] == '0':
                return s[:pos-1] + '0' + s[pos+2:]
            elif s[pos-1] == '1' and s[pos+1] == '0':
                return s[:pos-1] + '1' + s[pos+2:]
            elif s[pos-1] == '0' and s[pos+1] == '1':
                return s[:pos-1] + '1' + s[pos+2:]
            elif s[pos-1] == '1' and s[pos+1] == '1':
                return s[:pos-1] + '1' + s[pos+2:]
        if s[pos] == '&':
            if s[pos-1] == '0' and s[pos+1] == '0':
                return s[:pos-1] + '0' + s[pos+2:]
            elif s[pos-1] == '1' and s[pos+1] == '0':
                return s[:pos-1] + '0' + s[pos+2:]
            elif s[pos-1] == '0' and s[pos+1] == '1':
                return s[:pos-1] + '0' + s[pos+2:]
            elif s[pos-1] == '1' and s[pos+1] == '1':
                return s[:pos-1] + '1' + s[pos+2:]
        if s[pos] == '!':
            if s[pos+1] == '1' :
                return s[:pos] + '0' + s[pos+2:]
            elif s[pos+1] == '0' :
                return s[:pos] + '1' + s[pos+2:]

def find_y(s):
    op = ['!','&','+']
    while '(' in s:
        s = bracket(s)
    while any( x in s for x in op):
        s = calculate(s)
    return s

def find_out(t):
    v = count_var(t)
    y0 = eq(t,v)
    out = []
    for i in range(len(y0)):
        hold = []
        for j in range(len(y0[i])):
            hold.append(find_y(y0[i][j]))
        out.append(hold)
    return out
    
def print_out(t):
    var = count_var(t)
    out = find_out(t)
    for i in range(len(var)):
        c = 0
        if len(var[i]) == 0:
            print('input'+' '*25+'out')
            print(str(t[i])+' '*(30-len(t[i]))+str(out[i][0]))
            print('-'*60)
        else:
            s3 = ''
            c = 0
            print(str(var[i])+' '*(30-len(str(var[i])))+'out')
            c=0
            for j in range(len(out[i])):
                s = "{0:b}".format(c).zfill(len(var[i]))
                c+=1
                print(' '*(len(var[i])//2) + str(s)+' '*(30-len(s))+str(out[i][j]))
            print('-'*60)

def pretree(string):
    op = ('+','&')
    num = ('0','1','2','3','4','5','6','7','8','9')
    rout = []
    out = []
    stack = []
    c = 0
    p1 = False
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
        elif (any( n in string[i] for n in num) and string[i-1] != '|') and (any( n in string[i] for n in num) and string[i-1] != 'I'):
            rout.append(string[i])
    while len(stack) != 0:
        rout.append(stack.pop())
    while len(rout) != 0:
        out.append(rout.pop())
    return out

print_out(t)
