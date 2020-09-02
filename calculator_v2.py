import sys , pygame
from math import cos, sin, sqrt, tan


#-----------------------------------------------------------------------------
# customizable value

front = None
front_size = 40
line_thickness = 1
charactor_color = (0,0,100)
background_color = (255,255,255)
line_color = (200,200,200)
scr_w , scr_h = 500 , 700
refresh_rate = 10
image_name = 'image.jpg'
caption = 'calculator'
layout =[['Display'],
        ['Ans'],
        ['sin('  ,'cos('  ,'tan('  ,'sqrt(' ,'x^n'],
        ['7'    ,'8'    ,'9'    ,'delete'   ,'clear'],
        ['4'    ,'5'    ,'6'    ,'x'    ,'/'],
        ['1'    ,'2'    ,'3'    ,'+'    ,'-'],
        ['.'     ,'0'    ,'('    ,')'     ,'=']]

#-----------------------------------------------------------------------------
"""
key mapping

Num 0-9 or Numpad 0-9 == 0-9
. or Numpad . == point (.)
enter == equal (=)
Numpad + == plus (+)
Numpad * == multiply (x)
Numpad / == divided (/)
F1 == Sin(x)
F2 == Cos(x)
F3 == Tan(x)
F4 == Sqrt(x)
F5 == x^(n)

##sin,cos and tan using Radian

F12 == History Log

"""
#------------------------------------------------------------------------------


path = sys.path[0]
try:
    bg_image = pygame.image.load(path+'\\'+image_name)
except:
    bg_image = None


Ans_pos = [i for i in range(len(layout)) if layout[i] == ['Ans']]
Ans_pos = Ans_pos[0]
Dis_pos = [i for i in range(len(layout)) if layout[i] == ['Display']]
Dis_pos = Dis_pos[0]


def draw():
    for i in range(len(layout)):
        if layout[i] != ['Display']:
            if layout[i] != ['Ans']:            
                for j in range(len(layout[i])):
                    height = (scr_h//len(layout))
                    width = (scr_w//len(layout[i]))
                    screen.blit(font.render(layout[i][j],True,charactor_color), (10+j*width,50+i*height))
                    pygame.draw.line(screen,line_color,(j*width,i*height) , ((j)*width,(i+1)*height) ,line_thickness)
                    pygame.draw.line(screen,line_color,(j*width,i*height) , ((j+1)*width,(i)*height) ,line_thickness)


class calculator:
    def __init__(self):
        self.eq = ''
        self.ans = ''
        self.history = []

    def add(self,char):
        self.eq +=char
        
    def get_ans(self):
        temp = self.eq
        while 'x' in temp:
            pos = temp.find('x')
            temp = temp[:pos] + '*' + temp[pos+1:]
        while '^(' in temp:
            pos = temp.find('^(')
            temp = temp[:pos] + '**' + temp[pos+1:]
        try:
            self.ans = eval(temp)
            self.add_history()
        except:
            self.ans = 'SyntaxError'
    
    def delete(self):
        try:
            if self.eq[-4:] == 'sin(' or self.eq[-4:] == 'cos(' or self.eq[-4:] == 'tan(':
                self.eq = self.eq[:-4]
            elif self.eq[-2:] == '^(':
                self.eq = self.eq[:-2]
            elif self.eq[-5:] == 'sqrt(':
                self.eq = self.eq[:-5]
            else:
                self.eq = self.eq[:-1]
        except:
            pass

    def clear(self):
        self.eq = ''
        self.ans = ''

    def add_history(self):
        try:
            if self.history[-1][0] != self.eq and self.history[-1][1] != self.ans:
                self.history.append([self.eq,self.ans])
        except:
            self.history.append([self.eq,self.ans])
        if len(self.history) >= 10:
            self.history = self.history[-10:]



pygame.init()
pygame.display.set_caption(caption)
font = pygame.font.SysFont(front,front_size)
screen = pygame.display.set_mode( (scr_w, scr_h) )
h = scr_h // len(layout)
if bg_image == None:
    screen.fill(background_color)
else:
    bg_image = pygame.transform.scale(bg_image,(scr_w,scr_h))
    screen.blit(bg_image,(0,0))
draw()
pygame.display.update()
clock = pygame.time.Clock()
cal = calculator()


running = True
while running == True:
    clock.tick(refresh_rate)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)
            if key == '0' or key == '[0]':
                cal.add('0')
            elif key == '1' or key == '[1]':
                cal.add('1')
            elif key == '2' or key == '[2]':
                cal.add('2')
            elif key == '3' or key == '[3]':
                cal.add('3')
            elif key == '4' or key == '[4]':
                cal.add('4')
            elif key == '5' or key == '[5]':
                cal.add('5')
            elif key == '6' or key == '[6]':
                cal.add('6')
            elif key == '7' or key == '[7]':
                cal.add('7')
            elif key == '8' or key == '[8]':
                cal.add('8')
            elif key == '9' or key == '[9]':
                cal.add('9')

            elif key == '.' or key == '[.]':
                cal.add('.') 

            elif key == '[+]':
                cal.add('+')
            elif key == '[-]':
                cal.add('-')
            elif key == '[*]' or key == 'x':
                cal.add('x')
            elif key == '[/]':
                cal.add('/')

            elif key == '[':
                cal.add('(')
            elif key == ']':
                cal.add(')')

            elif key == 'backspace':
                cal.delete()
            elif key == 'delete':
                cal.clear() 
            elif key == 'return' or key == 'enter':
                cal.get_ans()

            elif key == 'f1':
                cal.add('sin(')
            elif key == 'f2':
                cal.add('cos(')
            elif key == 'f3':
                cal.add('tan(')
            elif key == 'f4':
                cal.add('sqrt(')
            elif key == 'f5':
                cal.add('^(')
            elif key == 'f12':
                mode = True
                blit = True
                while mode:
                    if blit:
                        screen.blit(bg_image,(0,0))
                        screen.blit(font.render('History Log',True,charactor_color),(10,30))
                        for i in range(6):
                            try:
                                screen.blit(font.render(str(cal.history[i][0]),True,charactor_color),(10,h//2+30+2*h//2*i))
                                screen.blit(font.render(str(cal.history[i][1]),True,charactor_color),(10,h//2+30+h//2*(1+2*i)))
                                pygame.display.update()
                            except:
                                pass
                        blit = False

                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            key = pygame.key.name(event.key)
                            if key == 'f12':
                                mode = False

            
            if bg_image == None:
                screen.fill(background_color)
            else:
                screen.blit(bg_image,(0,0))

            draw()
            screen.blit(font.render(cal.eq,True,charactor_color),(10,30+h*Dis_pos))
            screen.blit(font.render(str(cal.ans),True,charactor_color),(scr_w-17*len(str(cal.ans))-10,30+h*Ans_pos))
            pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x , y = pygame.mouse.get_pos()       
            r = y//(scr_h//len(layout))
            c = x//(scr_w//len(layout[r])) 
            if layout[r][c] == '=':
                cal.get_ans()

            elif layout[r][c] == 'delete':
                cal.delete()

            elif layout[r][c] == 'clear':
                cal.clear()

            elif layout[r][c] == 'sin' or layout[r][c] == 'cos' or layout[r][c] == 'tan':
                cal.add(layout[r][c])

            elif layout[r][c] == 'x^n':
                cal.add('^(')

            elif layout[r][c] != 'Display' and layout[r][c] != 'Ans':
                cal.add(str(layout[r][c]))
        
            if bg_image == None:
                screen.fill(background_color)
            else:
                screen.blit(bg_image,(0,0))

            draw()
            screen.blit(font.render(cal.eq,True,charactor_color),(10,30+h*Dis_pos))
            screen.blit(font.render(str(cal.ans),True,charactor_color),(scr_w-17*len(str(cal.ans))-10,30+h*Ans_pos))
            pygame.display.update()
