def count_var(text_list):
    var_list = []
    var = ('|','I')
    for i in range(len(text_list)):
        list_out = []
        string = text_list[i]
        for j in range(len(string)):
            if string[j].isupper() and string[j] != 'I':
                if not string[j] in list_out:
                    list_out.append(string[j])
            elif any(v in string[j] for v in var):
                if not string[j:j+2] in list_out:
                    list_out.append(string[j:j+2])
        var_list.append(list_out)
    return var_list

def expression_list(text_list,var_list):
    expression = []
    for i in range(len(text_list)):
        sub_expression = []
        if len(var_list[i]) != 0: 
            c = 0
            temp = text_list[i]
            for j in range(2**len(var_list[i])):
                binary = "{0:b}".format(c).zfill(len(var_list[i]))
                for k in range(len(binary)):
                    while var_list[i][k] in temp:
                        pos = temp.find(var_list[i][k])
                        if'I' in var_list[i][k]:
                            temp = temp[:pos] + binary[k] + temp[pos+2:]
                        elif '|' in var_list[i][k]:
                            temp = temp[:pos] + binary[k] + temp[pos+2:]
                        elif var_list[i][k].isupper():
                            temp = temp[:pos] + binary[k] + temp[pos+1:]
                sub_expression.append(temp)
                temp = text_list[i]
                c += 1
        else:
            sub_expression.append(text_list[i])
            expression.append(sub_expression)
            sub_expression = []
        if sub_expression != []:
            expression.append(sub_expression)
    return expression

def count(expression_string,start,last):
    c = 0
    st = False
    for i in range(last-start):
        if expression_string[start+i] == '(':
            c += 1
            st = True
        elif expression_string[start+i] == ')':
            c -= 1
        if c == 0 and st == True:
            return start+i

def bracket(expression_string):
    pos = expression_string.find('(')
    c = count(expression_string,pos,len(expression_string))
    return expression_string[:pos] + calculate(expression_string[pos+1:c]) + expression_string[c+1:]

def calculate(expression_string):
    operator = ['!','&','+']
    if len(expression_string) == 1:
        return expression_string
    if '(' in expression_string:
        pos = expression_string.find('(')
        c = count(expression_string,pos,len(expression_string))
        return expression_string[:pos] + calculate(expression_string[pos+1:c]) + expression_string[c+1:]
    while any( op in expression_string for op in operator):
        for op in operator:    
            pos = expression_string.rfind(op)
            if pos != -1:
                break
        if expression_string[pos] == '+':
            if expression_string[pos-1] == '0' and expression_string[pos+1] == '0':
                return expression_string[:pos-1] + '0' + expression_string[pos+2:]
            elif expression_string[pos-1] == '1' and expression_string[pos+1] == '0':
                return expression_string[:pos-1] + '1' + expression_string[pos+2:]
            elif expression_string[pos-1] == '0' and expression_string[pos+1] == '1':
                return expression_string[:pos-1] + '1' + expression_string[pos+2:]
            elif expression_string[pos-1] == '1' and expression_string[pos+1] == '1':
                return expression_string[:pos-1] + '1' + expression_string[pos+2:]
        if expression_string[pos] == '&':
            if expression_string[pos-1] == '0' and expression_string[pos+1] == '0':
                return expression_string[:pos-1] + '0' + expression_string[pos+2:]
            elif expression_string[pos-1] == '1' and expression_string[pos+1] == '0':
                return expression_string[:pos-1] + '0' + expression_string[pos+2:]
            elif expression_string[pos-1] == '0' and expression_string[pos+1] == '1':
                return expression_string[:pos-1] + '0' + expression_string[pos+2:]
            elif expression_string[pos-1] == '1' and expression_string[pos+1] == '1':
                return expression_string[:pos-1] + '1' + expression_string[pos+2:]
        if expression_string[pos] == '!':
            if expression_string[pos+1] == '1' :
                return expression_string[:pos] + '0' + expression_string[pos+2:]
            elif expression_string[pos+1] == '0' :
                return expression_string[:pos] + '1' + expression_string[pos+2:]

def calculate_expression(expression_string):
    operator = ['!','&','+']
    while '(' in expression_string:
        expression_string = bracket(expression_string)
    while any( op in expression_string for op in operator):
        expression_string = calculate(expression_string)
    return expression_string

def output_list(text_list):
    var = count_var(text_list)
    exp = expression_list(text_list,var)
    output = []
    for i in range(len(exp)):
        temp = []
        for j in range(len(exp[i])):
            temp.append(calculate_expression(exp[i][j]))
        output.append(temp)
    return output

def print_output(text_list,i):
    var = count_var(text_list)
    out = output_list(text_list)
    if len(var[i]) == 0:
        print('input'+' '*25+'out')
        print(str(text_list[i])+' '*(30-len(text_list[i]))+str(out[i][0]))
        print('-'*60)
    else:
        dec = 0
        print(str(var[i])+' '*(30-len(str(var[i])))+'out')
        temp = []
        for j in range(len(out[i])):
            binary = "{0:b}".format(dec).zfill(len(var[i]))
            for k in range(len(str(binary))):
                temp.append(binary[k])
            dec+=1
            print(' '*(len(var[i])//2) + str(temp)+' '*(30-len(str(temp)))+str(out[i][j]))
            temp = []
        print('-'*60)

def prefix_str(string):
    print(string)
    operator = ('+','&')
    number = ('0','1')
    reverse_output = []
    output = []
    stack = []
    counter = 0
    inverse = False
    digit = False
    and_check = False
    primary = False
    for i in range(len(string)):
        if string[i] == '(':
            and_check = False
            inverse = False
            if reverse_output != [] and i != 0:
                if string[i-1] == '+':
                    primary = True     
                if primary == True and string[i-1] == '&':
                    temp = stack.pop()
                    stack.append(reverse_output.pop())
                    stack.append(temp)
                    primary = False
        elif string[i] == ')':
            if stack != []:
                reverse_output.append(stack.pop())

            if counter == 2:
                if stack != []:
                    reverse_output.append(stack.pop())
            
            counter = 0
            inverse = False

        elif string[i] == '!':
            if string[i+1] == 'I' or string[i+1] == '|' or string[i+1].isupper():
                if string[i+1].isupper() and string[i+1] != 'I':
                    reverse_output.append(string[i:i+2])
                else:
                    reverse_output.append(string[i:i+3])
                    digit = True
                counter += 1
                inverse = True
            else:
                stack.append(string[i])

        elif any( op in string[i] for op in operator):
            if string[i] == '+':
                stack.append(string[i])
            else:
                stack.append(string[i])
                and_check = True
                if counter != 0:
                    counter -= 1
            if counter == 2:
                counter = 0
                reverse_output.append(stack.pop())
            
        elif string[i] == '|' or string[i] == 'I':
            if inverse != True:
                reverse_output.append(string[i:i+2])
                counter += 1
                digit = True
            else:
                inverse = False
            if and_check == True:
                and_check = False
                if stack != []:
                    reverse_output.append(stack.pop())


        elif string[i].isdigit():
            if digit == False:
                reverse_output.append(string[i])
            else:
                digit = False
            if and_check == True:
                and_check = False
                if stack != []:
                    reverse_output.append(stack.pop())
                    counter += 1
        elif string[i].isupper():
            if inverse != True:
                if i == len(string)-1:
                    reverse_output.append(string[i])
                    counter += 1
                    if counter == 2:
                        counter = 0
                        reverse_output.append(stack.pop())
                elif not string[i+1].isdigit():
                    reverse_output.append(string[i])
                    counter += 1
                    if counter == 2:
                        counter = 0
                        reverse_output.append(stack.pop())
                if and_check == True:
                    if stack != []:
                        reverse_output.append(stack.pop())

    while len(stack) != 0:
        reverse_output.append(stack.pop())
    while len(reverse_output) != 0:
        output.append(reverse_output.pop())
    return output