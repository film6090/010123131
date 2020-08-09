import pygame , math

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

def mathfunction(eq_str):
    pos = eq_str.find('sqrt')
    if pos != (-1):    
        c = count(eq_str,pos,len(eq_str))
        if any( x in eq_str[pos:c] for x in angle) or 'sqrt' in eq_str[pos:c]: 
            return eq_str[:pos]+str(math.sqrt(float(calculate(mathfunction(eq_str[pos+5:c])))))+eq_str[c+1:]
        
        elif any( x in eq_str[pos:c] for x in bracket):
            return eq_str[:pos]+str(math.sqrt(float(calculate(bracket(eq_str[pos+5:c])))))+eq_str[c+1:]
        
        elif any( x in eq_str[pos:c] for x in operator):
            return eq_str[:pos]+str(math.sqrt(float(calculate(eq_str[pos+5:c]))))+eq_str[c+1:]
        
        else:
            return eq_str[:pos]+str(math.sqrt(float(eq_str[pos+5:c])))+eq_str[c+1:]
    
    for t in angle:
        pos = eq_str.find(t)
        if pos != (-1):
            break
    
    c = count(eq_str,pos,len(eq_str))
    if eq_str[pos:pos+3] == 'sin':
        if any( x in eq_str[pos:c] for x in angle) or 'sqrt' in eq_str[pos:c]:
            return eq_str[:pos]+str(math.sin(math.radians(float(calculate(mathfunction(eq_str[pos+4:c]))))))+eq_str[c+1:]
    
        elif any( x in eq_str[pos:c] for x in bracket):
            return eq_str[:pos]+str(math.sin(math.radians(float(calculate(bracket(eq_str[pos+4:c]))))))+eq_str[c+1:]
    
        elif any( x in eq_str[pos:c] for x in operator):
            return eq_str[:pos]+str(math.sin(math.radians(float(calculate(eq_str[pos+4:c])))))+eq_str[c+1:]
    
        else:
            return eq_str[:pos]+str(math.sin(math.radians(float(eq_str[pos+4:c]))))+eq_str[c+1:]


    elif eq_str[pos:pos+3] == 'cos':
        if any( x in eq_str[pos:c] for x in angle) or 'sqrt' in eq_str[pos:c]: 
            return eq_str[:pos]+str(math.cos(math.radians(float(calculate(mathfunction(eq_str[pos+4:c]))))))+eq_str[c+1:]
        
        elif any( x in eq_str[pos:c] for x in bracket):
            return eq_str[:pos]+str(math.cos(math.radians(float(calculate(bracket(eq_str[pos+4:c]))))))+eq_str[c+1:]
        
        elif any( x in eq_str[pos:c] for x in operator):
            return eq_str[:pos]+str(math.cos(math.radians(float(calculate(eq_str[pos+4:c])))))+eq_str[c+1:]
        
        else:
            return eq_str[:pos]+str(math.cos(math.radians(float(eq_str[pos+4:c]))))+eq_str[c+1:]


    elif eq_str[pos:pos+3] == 'tan':
        if any( x in eq_str[pos:c] for x in angle) or 'sqrt' in eq_str[pos:c]: 
            return eq_str[:pos]+str(math.tan(math.radians(float(calculate(mathfunction(eq_str[pos+4:c]))))))+eq_str[c+1:]
        
        elif any( x in eq_str[pos:c] for x in bracket):
            return eq_str[:pos]+str(math.tan(math.radians(float(calculate(bracket(eq_str[pos+4:c]))))))+eq_str[c+1:]
        
        elif any( x in eq_str[pos:c] for x in operator):
            return eq_str[:pos]+str(math.tan(math.radians(float(calculate(eq_str[pos+4:c])))))+eq_str[c+1:]
        
        else:
            return eq_str[:pos]+str(math.tan(math.radians(float(eq_str[pos+4:c]))))+eq_str[c+1:]
    else:
        return eq_str



def bracket(eq_str):
    pos = eq_str.find('(')
    c = count(eq_str,pos,len(eq_str))
    if (any(x in eq_str[pos:c] for x in angle) or 'sqrt' in eq_str[pos:c]) == True:
        return eq_str[:pos] + str(mathfunction(eq_str[pos+1:c])) + eq_str[c+1:]
    elif '(' in eq_str[pos:c]:
        return eq_str[:pos] + str(bracket(eq_str[pos+1:c])) + eq_str[c+1:]
    elif any( x in sqrt[pos:c] for x in operator):
        return eq_str[:pos] + str(calculate(eq_str[pos+1:c])) + eq_str[c+1:]
    else:
        return eq_str[:pos] + eq_str[pos+1:c] + eq_str[c+1:]

def calculate(eq_str):
    if any( x in eq_str for x in angle):
        return calculate(mathfunction(eq_str))
    for t in operator:
        pos = eq_str.find(t)
        if pos != (-1):
            break
    if eq_str[pos] == '+':
        return float(calculate(eq_str[:pos])) + float(calculate(eq_str[pos+1:]))

    elif eq_str[pos] == '-':
        return float(calculate(eq_str[:pos])) - float(calculate(eq_str[pos+1:]))

    elif eq_str[pos] == 'x':
        return  float(calculate(eq_str[:pos])) * float(calculate(eq_str[pos+1:]))

    elif eq_str[pos] == '/':
        return  float(calculate(eq_str[:pos])) / float(calculate(eq_str[pos+1:]))
    else:
        return eq_str

equation = ''
ans = 0
operator = ['+','-','x','/']
angle = ['sin','cos','tan']
power = ['sqrt', '^']
layout =    (('','','','',''),
            ('sin('  ,'cos('  ,'tan('  ,'sqrt(' ,''),
            ('7'    ,'8'    ,'9'    ,'delete'   ,'clear'),
            ('4'    ,'5'    ,'6'    ,'x'    ,'/'),
            ('1'    ,'2'    ,'3'    ,'+'    ,'-'),
            ('.'     ,'0'    ,'('    ,')'     ,'='))

def draw():
    for i in range(len(layout)):
        for j in range(len(layout[i])):
            screen.blit(font.render(layout[i][j],True,(0,0,0)), (20+j*(scr_w//len(layout[0])),50+i*(scr_h//len(layout))))

pygame.init()
font = pygame.font.SysFont(None,40)
scr_w , scr_h = 500 , 600
screen = pygame.display.set_mode( (scr_w, scr_h) )
screen.fill((255,255,255))
w,h = 100,100
draw()
pygame.display.update()

running = True
while running == True:
    pygame.display.update()
    for event in pygame.event.get():

        screen.fill((255,255,255))
        draw()
        screen.blit(font.render(str(ans),True,(0,0,0)),(scr_w-17*len(str(ans))-10,90))
        screen.blit(font.render(equation,True,(0,0,0)),(10,10))

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x , y = pygame.mouse.get_pos()
            c , r = x//w , y//h
            eq = equation
            if layout[r][c] == '=':
                while any( x in eq for x in angle)  or 'sqrt' in eq:
                    eq = mathfunction(eq)
                while '(' in eq == True:
                    eq = bracket(eq)
                if any( x in eq for x in operator):
                    if eq[0] != '-':
                        if '+' in eq:
                            pos = eq.find('+')
                            eq = eq[pos+1:] + eq[:pos]
                            ans = calculate(eq)
                        elif 'x' in eq:
                            ans = '-' + calculate[1:]
                        elif  '/' in eq:
                            ans = '-' + calculate[1:]
                        else:
                            ans = calculate(eq)
                    else:
                        ans = eq
                else:
                    ans = eq
                screen.blit(font.render(str(ans),True,(0,0,0)),(scr_w-17*len(str(ans))-10,90))

            elif layout[r][c] == 'delete':
                if any(x in equation[-4:] for x in angle):
                    equation = equation[:-4]
                else:
                    equation = equation[:-1]

            elif layout[r][c] == 'clear':
                eq = ''
                equation = ''
                ans = 0

            elif layout[r][c] == 'sin' or layout[r][c] == 'cos' or layout[r][c] == 'tan':
                equation += str(layout[r][c])
                screen.blit(font.render(equation,True,(0,0,0)),(10,10))

            elif layout[r][c] == 'x^n':
                equation += '^('

            else:
                equation += str(layout[r][c])
                screen.blit(font.render(equation,True,(0,0,0)),(10,10))

