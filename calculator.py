import math , pygame

refresh_rate = 30
def draw():
    for i in range(len(layout)):
        for j in range(len(layout[i])):
            screen.blit(font.render(layout[i][j],True,(0,0,0)), (20+j*(scr_w//len(layout[0])),50+i*(scr_h//len(layout))))

equation = ['','']
layout =    (('','','','',''),
            ('sin'  ,'cos'  ,'tan'  ,'sqrt' ,'x^n'),
            ('7'    ,'8'    ,'9'    ,'delete'   ,'clear'),
            ('4'    ,'5'    ,'6'    ,'*'    ,'/'),
            ('1'    ,'2'    ,'3'    ,'+'    ,'-'),
            ('.'     ,'0'    ,'('    ,')'     ,'='))

pygame.init()
font = pygame.font.SysFont(None,40)
scr_w , scr_h = 500 , 600
screen = pygame.display.set_mode( (scr_w, scr_h) )
screen.fill((255,255,255))
w,h = 100,100
draw()
pygame.display.update()
ans = 0
ang = False
running = True
while running == True:
    for event in pygame.event.get():
        screen.fill((255,255,255))
        draw()
        screen.blit(font.render(str(ans),True,(0,0,0)),(scr_w-17*len(str(ans))-10,90))
        screen.blit(font.render(equation[0],True,(0,0,0)),(10,10))
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x , y = pygame.mouse.get_pos()
            c , r = x//w , y//h


            if layout[r][c] == '=':
                ans = eval(equation[1])
                screen.blit(font.render(str(ans),True,(0,0,0)),(scr_w-17*len(str(ans))-10,90))
            
            
            elif layout[r][c] == 'delete':
                if ang == True:
                    for i in range(1+len(last)):
                        equation[0] = equation[0][:-1]
                    for i in range(6+len(last)):
                        equation[1] = equation[0][:-1]
                    
                else:
                    equation[0] = equation[0][:-1]
                    equation[1] = equation[1][:-1]
                
                last = ''
                ang = False
                
            
            
            elif layout[r][c] == 'clear':
                equation[0],equation[1] = '',''
                ans = 0
                ang = False
            
            
            elif layout[r][c] == 'sin' or layout[r][c] == 'cos' or layout[r][c] == 'tan' or layout[r][c] == 'sqrt':
                ang = True
                last = layout[r][c]
                equation[0] += str(layout[r][c])+'('
                equation[1] += 'math.' + str(layout[r][c]) + '('
                screen.blit(font.render(equation[0],True,(0,0,0)),(10,10))
                
            
            elif layout[r][c] == 'x^n':
                equation[0] += '^('
                equation[1] += '**('
                ang = False
            
            else:
                equation[0] += str(layout[r][c])
                equation[1] += str(layout[r][c])
                screen.blit(font.render(equation[0],True,(0,0,0)),(10,10))
                ang = False
        pygame.display.update()
                