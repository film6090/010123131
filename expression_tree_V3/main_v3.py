import pygame , sys
from my_function_v3 import prefix_str,print_output,calculate_expression

path = sys.path[0]
file_name = 'text_for_v3.txt'
f = open( path + '\\' + file_name , 'r' )
text_list = f.readlines()


for i in range(len(text_list)):
    if i != len(text_list)-1:
        text_list[i] = text_list[i][4:len(text_list[i])-2]
        
    else:
        text_list[i] = text_list[i][4:len(text_list[i])-1]

        
def draw(input_list,position,half,height=0,list_index=0,scenario=0):
    global start
    pygame.display.update()
    operator = ['+','&']
    h = scr_h//5
    
    
    if height != 0 and scenario == 0:
        pygame.draw.line(screen,(100,100,100),(position,h*height+50),(position-2*half+20,h*(height-1)+50),10)
    
    elif height != 0 and scenario == 1:
        pygame.draw.line(screen,(100,100,100),(position,h*height+50),(position+2*half-20,h*(height-1)+50),10)
    
    elif height != 0 and scenario == 2:
         pygame.draw.line(screen,(100,100,100),(position,h*height+50),(position,h*(height-1)+70),10)
    
    if input_list[list_index] == '!':
        pygame.draw.circle(screen,(100,100,100),(position,h*height+50),30)
        screen.blit(font.render(input_list[list_index],True,(0,255,100)),(position-10,h*height+38))
        draw(input_list,position,half,height+1,list_index+1,2)
    
    elif any( x in input_list[list_index] for x in operator):
        pygame.draw.circle(screen,(100,100,100),(position,h*height+50),30)
        screen.blit(font.render(input_list[list_index],True,(0,255,100)),(position-10,h*height+38))
        draw(input_list,position+half,half//2,height+1,list_index+1)
        draw(input_list,position-half,half//2,height+1,start+1,1)
    
    else:
        pygame.draw.circle(screen,(100,100,100),(position,h*height+50),30)
        screen.blit(font.render(input_list[list_index],True,(0,255,100)),(position-10,h*height+38))
        start = list_index

start = 0
i = 0
scr_w , scr_h = 1000 , 600

pygame.init()
font = pygame.font.SysFont(None,40)
screen = pygame.display.set_mode( (scr_w, scr_h) )
screen.fill((255,255,255))
draw(y,scr_w//2,scr_w//4)
screen.blit(font.render(text_list[i],True,(200,100,150)),(20,25))
screen.blit(font.render('click to go to next expression',True,(200,100,150)),(scr_w-400,25))
pygame.display.update()


y = prefix_str(text_list[i])
print_output(text_list,i)


running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if len(text_list)-1 != i:
                i+=1
                print_output(text_list,i)
                
                y = prefix_str(text_list[i])
                screen.fill((255,255,255))
                draw(y,scr_w//2,scr_w//4)
                screen.blit(font.render(text_list[i],True,(200,100,150)),(20,25))
                screen.blit(font.render('click to go to next expression',True,(200,100,150)),(scr_w-400,25))
                pygame.display.update()
                
                
            else:
                running = False

pygame.quit()


