class function:
    def __init__(self,text_str):
        self.text = text_str
        self.prefix = self.prefix_str()
        self.var = self.count_var()
        self.possible_expression = self.expression_list()
        self.output = self.calculate_expression()
        
    def prefix_str(self):
        operator = ('+','&')
        counter = 0
        reverse_output = []
        output = []
        stack = []
        inverse = False
        digit = False
        and_check = False
        primary = False

        for i in range(len(self.text)):
            if self.text[i] == '(':
                and_check = False
                inverse = False

                if reverse_output != [] and i != 0:
                    if self.text[i-1] == '+':
                        primary = True     

                    if primary == True and self.text[i-1] == '&':
                        temp = stack.pop()
                        stack.append(reverse_output.pop())
                        stack.append(temp)
                        primary = False

            elif self.text[i] == ')':
                if stack != []:
                    reverse_output.append(stack.pop())

                if counter == 2:
                    if stack != []:
                        reverse_output.append(stack.pop())
                
                counter = 0
                inverse = False

            elif self.text[i] == '!':
                if self.text[i+1] == 'I' or self.text[i+1] == '|' or self.text[i+1].isupper():
                    if self.text[i+1].isupper() and self.text[i+1] != 'I':
                        reverse_output.append(self.text[i:i+2])

                    else:
                        reverse_output.append(self.text[i:i+3])
                        digit = True

                    counter += 1
                    inverse = True

                else:
                    stack.append(self.text[i])

            elif any( op in self.text[i] for op in operator):
                if self.text[i] == '+':
                    stack.append(self.text[i])

                else:
                    stack.append(self.text[i])
                    and_check = True

                    if counter != 0:
                        counter -= 1

                if counter == 2:
                    counter = 0
                    reverse_output.append(stack.pop())
                
            elif self.text[i] == '|' or self.text[i] == 'I':
                if inverse != True:
                    reverse_output.append(self.text[i:i+2])
                    counter += 1
                    digit = True

                else:
                    inverse = False

                if and_check == True:
                    and_check = False

                    if stack != []:
                        reverse_output.append(stack.pop())

            elif self.text[i].isdigit():
                if digit == False:
                    reverse_output.append(self.text[i])

                else:
                    digit = False

                if and_check == True:
                    and_check = False

                    if stack != []:
                        reverse_output.append(stack.pop())
                        counter += 1

            elif self.text[i].isupper():
                if inverse != True:
                    if i == len(self.text)-1:
                        reverse_output.append(self.text[i])
                        counter += 1

                        if counter == 2:
                            counter = 0
                            reverse_output.append(stack.pop())

                    elif not self.text[i+1].isdigit():
                        reverse_output.append(self.text[i])
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


    def count_var(self):
        var = ('|','I')
        list_out = []

        for j in range(len(self.text)):
            if self.text[j].isupper() and self.text[j] != 'I':
                if not self.text[j] in list_out:
                    list_out.append(self.text[j])

            elif any(v in self.text[j] for v in var):
                if not self.text[j:j+2] in list_out:
                    list_out.append(self.text[j:j+2])

        return list_out


    def expression_list(self):
        expression = []

        if len(self.var) != 0:
            c = 0
            temp = self.text

            for _ in range(2**len(self.var)):
                binary = "{0:b}".format(c).zfill(len(self.var))

                for i in range(len(binary)):
                    while self.var[i] in temp:
                        pos = temp.find(self.var[i])

                        if'I' in self.var[i]:
                            temp = temp[:pos] + binary[i] + temp[pos+2:]

                        elif '|' in self.var[i]:
                            temp = temp[:pos] + binary[i] + temp[pos+2:]

                        elif self.var[i].isupper():
                            temp = temp[:pos] + binary[i] + temp[pos+1:]

                c += 1
                expression.append(temp)
                temp = self.text

        else:
            expression.append(self.text)

        return expression


    def calculate_expression(self):
        operator = ['!','&','+']
        output = []

        for i in range(len(self.possible_expression)):
            temp = self.possible_expression[i]

            while '(' in temp:
                temp = bracket(temp)

            while any( op in temp for op in operator):
                temp = calculate(temp)

            output.append(temp)

        return output
                

    def print_output(self):
        if len(self.var) == 0:
            print('input'+' '*25+'out')
            print(str(self.text)+' '*(30-len(self.text))+str(self.output[0]))
            print('-'*60)

        else:
            dec = 0
            temp = []
            print(str(self.var)+' '*(30-len(str(self.var)))+'out')

            for i in range(len(self.output)):
                binary = "{0:b}".format(dec).zfill(len(self.var))

                for j in range(len(str(binary))):
                    temp.append(binary[j])

                print(' '*(len(self.var)//2) + str(temp)+' '*(30-len(str(temp)))+str(self.output[i]))
                dec += 1
                temp = []

            print('-'*60)


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


def bracket(expression_string):
    pos = expression_string.find('(')
    c = count(expression_string,pos,len(expression_string))
    return expression_string[:pos] + calculate(expression_string[pos+1:c]) + expression_string[c+1:]


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

