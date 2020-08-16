import pygame
from prefix import pretree

op = ['&','+']
t = ['!(|0&|1)+!(|1+|2)','(((I0&I1&!I2)+!I1)+I3)',"!(I1+I0)","!(!(|0+I0&|1))","(I0+!I1+!(I2))&(!I0+I1+I2)"]

def draw(output_list,pos,half,i=0,j=0,s=0):
    pygame.display.update()
    height = 100
    mid = ((len(output_list)+1)//2)
    if i != 0 and s == 0:
        pygame.draw.line(screen,(255,255,255),(pos,height*i+50),(pos+2*half-20,height*(i-1)+50),10)
    elif i != 0 and s == 1:
        pygame.draw.line(screen,(255,255,255),(pos,height*i+50),(pos-2*half+20,height*(i-1)+50),10)
    elif i != 0 and s == 3:
         pygame.draw.line(screen,(255,255,255),(pos,height*i+50),(pos,height*(i-1)+70),10)
    if output_list[j] == '!':
        pygame.draw.circle(screen,(255,255,255),(pos,height*i+50),30)
        screen.blit(font.render(output_list[j],True,(0,255,0)),(pos-10,height*i+38))
        draw(output_list,pos,half,i+1,j+1,3)
    elif i == 0:
        pygame.draw.circle(screen,(255,255,255),(pos,height*i+50),30)
        screen.blit(font.render(output_list[j],True,(0,255,0)),(pos-10,height*i+38))
        if any(x in output_list[mid] for x in op) or '!' == output_list[mid]:
            draw(output_list,pos-half,half//2,i+1,j+1)
            draw(output_list,pos+half,half//2,i+1,mid,1)
        else:
            draw(output_list,pos-half,half//2,i+1,j+1)
            draw(output_list,pos+half,half//2,i+1,j+2,1)
    elif output_list[j] == '+' or output_list[j] == '&':
        pygame.draw.circle(screen,(255,255,255),(pos,height*i+50),30)
        screen.blit(font.render(output_list[j],True,(0,255,0)),(pos-10,height*i+38))
        draw(output_list,pos-half,half//2,i+1,j+1)
        draw(output_list,pos+half,half//2,i+1,j+2,1)
    else:
        pygame.draw.circle(screen,(255,255,255),(pos,height*i+50),30)
        screen.blit(font.render(output_list[j],True,(0,255,0)),(pos-10,height*i+38))

pygame.init()
font = pygame.font.SysFont(None,40)
scr_w , scr_h = 1000 , 600
screen = pygame.display.set_mode( (scr_w, scr_h) )
screen.fill((0,0,0))
pygame.display.update()
i = 0
y = pretree(t[i])
print(y)
screen.fill((0,0,0))
draw(y,scr_w//2,scr_w//4)
pygame.display.update()

running = True
while running == True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if len(t)-1 != i:
                i+=1
                y = pretree(t[i])
                print(y)
                screen.fill((0,0,0))
                draw(y,scr_w//2,scr_w//4)
                pygame.display.update()
            else:
                running = False

pygame.quit()

