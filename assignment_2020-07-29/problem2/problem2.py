import pygame , random

def changebg(M_pos,N_pos,color=(0,0,0)):
    for i in range(h):
        for j in range(w):
            surface.set_at((M_pos*w+j,N_pos*h+i),color)
    screen.blit(surface,(0,0))
    pygame.display.update()


def swap(M_pos,N_pos,M_target,N_target):
    p1=pic[M_pos+M*N_pos]
    p2=pic[M_target+M*N_target]
    pic[M_pos+M*N_pos]=p2
    pic[M_target+M*N_target]=p1
    print(p1,p2)
    print(pic[p1],pic[p2])
    screen.blit(bg,((p1%M)*w,(p1//N)*h),((p2%M)*w,(p2//N)*h,w,h))
    screen.blit(bg,((p2%M)*w,(p2//N)*h),((p1%M)*w,(p1//N)*h,w,h))
    pygame.display.update()



M,N = 10,10
scr_w , scr_h = 500 , 500
pygame.init()
screen = pygame.display.set_mode( (scr_w, scr_h) )
bg = pygame.image.load(r"image_path").convert()
scr_w , scr_h = bg.get_width() , bg.get_height()
screen = pygame.display.set_mode( (scr_w, scr_h) )
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )
screen.blit(bg,(0,0))
w = scr_w//M
h = scr_h//N
pygame.display.update()
pic = [i for i in range(M*N)]



drag = False
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x1 , y1 = pygame.mouse.get_pos()
            c1 , r1 = x1//w , y1//h
            drag = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            x2 , y2 = pygame.mouse.get_pos()
            c2 , r2 = x2//w , y2//h
            if c1!=c2 and r1!=r2:
                swap(c1,r1,c2,r2)
                pygame.display.update()
            drag = False
