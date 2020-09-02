import pygame , sys
from math import sin , cos , tan , sqrt

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

path = sys.path[0]
try:
    bg_image = pygame.image.load(path+'\\'+image_name)
except:
    bg_image = None

equation = ''
ans = ''

Ans_pos = [i for i in range(len(layout)) if layout[i] == ['Ans']]
Ans_pos = Ans_pos[0]
dis_pos = [i for i in range(len(layout)) if layout[i] == ['Display']]
dis_pos = dis_pos[0]

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


running = True
while running == True:
    clock.tick(refresh_rate)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x , y = pygame.mouse.get_pos()       
            r = y//(scr_h//len(layout))
            c = x//(scr_w//len(layout[r])) 
            if layout[r][c] == '=':
                eq = equation
                while 'x' in eq:
                    pos = eq.find('x')
                    eq = eq[:pos] + '*' + eq[pos+1:]
                while '^(' in eq:
                    pos = eq.find('^(')
                    eq = eq[:pos] + '**' + eq[pos+1:]
                try:
                    ans = eval(eq)
                except:
                    ans = 'SyntaxError'

            elif layout[r][c] == 'delete':
                if any(x in equation[-4:] for x in angle):
                    equation = equation[:-4]
                elif equation[-2:] == '^(':
                    equation = equation[:-2]
                elif equation[-5:] == 'sqrt(':
                    equation = equation[:-5]
                else:
                    equation = equation[:-1]

            elif layout[r][c] == 'clear':
                equation = ''
                ans = ''

            elif layout[r][c] == 'sin' or layout[r][c] == 'cos' or layout[r][c] == 'tan':
                equation += str(layout[r][c])
                screen.blit(font.render(equation,True,charactor_color),(10,10))

            elif layout[r][c] == 'x^n':
                equation += '^('

            else:
                equation += str(layout[r][c])
                screen.blit(font.render(equation,True,charactor_color),(10,10))
        
            if bg_image == None:
                screen.fill(background_color)
            else:
                bg_image = pygame.transform.scale(bg_image,(scr_w,scr_h))
                screen.blit(bg_image,(0,0))

            draw()
            screen.blit(font.render(equation,True,charactor_color),(10,30+h*dis_pos))
            screen.blit(font.render(str(ans),True,charactor_color),(scr_w-17*len(str(ans))-10,30+h*Ans_pos))
            pygame.display.update()

