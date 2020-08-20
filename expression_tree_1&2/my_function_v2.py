def count_var(text_list):
    var_list = []
    var = ('|','I')
    
    for i in range(len(text_list)):
        list_out = []
        string = text_list[i]
        
        for j in range(text_list[i].count('|')+text_list[i].count('I')):
            pos = len(text_list[i])
            
            for x in var:
                pos_temp = string.find(x)
                
                if pos_temp != (-1):
                    
                    if pos > pos_temp:
                        pos = pos_temp
            
            if not(string[pos:pos+2] in list_out):
                list_out.append(string[pos:pos+2])
            
            string = string[pos+1:]
        
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
                        temp = temp[:pos] + binary[k] + temp[pos+2:]
                
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
    operator = ('+','&')
    number = ('0','1','2','3','4','5','6','7','8','9')
    reverse_output = []
    output = []
    stack = []
    counter = 0
    inverse = False
    print(string)
    
    for i in range(len(string)):
        if string[i] == ')':
            reverse_output.append(stack.pop())
            counter = 0
        
        elif string[i] == '!':
            if string[i+1] == 'I' or string[i+1] == '|':
                reverse_output.append(string[i:i+3])
                counter += 1
                inverse = True
                
                if counter == 2:
                    counter = 0
                    reverse_output.append(stack.pop())
            
            else:
                stack.append(string[i])
        
        elif any( op in string[i] for op in operator):
            stack.append(string[i])
        
        elif string[i] == '|' or string[i] == 'I':
            if inverse != True:
                reverse_output.append(string[i:i+2])
                counter += 1
        
                if counter == 2:
                    counter = 0
                    reverse_output.append(stack.pop())
            
            else:
                inverse = False
        
        elif (any( num in string[i] for num in number) and string[i-1] != '|') and (any( num in string[i] for num in number) and string[i-1] != 'I'):
            reverse_output.append(string[i])
    
    while len(stack) != 0:
        reverse_output.append(stack.pop())
    
    while len(reverse_output) != 0:
        output.append(reverse_output.pop())
    
    return output
