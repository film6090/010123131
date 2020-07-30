import pygame , random

#------------------------------------------------------------------------------------------
#function
def swap(M_pos,N_pos,M_target,N_target):
    p1=pic[M_pos][N_pos]
    p2=pic[M_target][N_target]
    pic[M_pos][N_pos]=p2
    pic[M_target][N_target]=p1
    screen.blit(bg,(M_pos*w,N_pos*h),((p2//M)*w,(p2%M)*h,w,h))
    screen.blit(bg,(M_target*w,N_target*h),((p1//M)*w,(p1%M)*h,w,h))
    pygame.display.update()

#------------------------------------------------------------------------------------------
#setup
M,N = 10,10
scr_w , scr_h = 500 , 500
pygame.init()
screen = pygame.display.set_mode( (scr_w, scr_h) )
bg = pygame.image.load(r"image_path").convert() # Ex. pygame.image.load(r"C:\user\user\desktop\image.jpg").convert
scr_w , scr_h = bg.get_width() , bg.get_height()
screen = pygame.display.set_mode( (scr_w, scr_h) )
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )
screen.blit(bg,(0,0))
w = scr_w//M
h = scr_h//N
pygame.display.update()
pic = [[i+(j*M) for i in range(M)]for j in range(N)]

#------------------------------------------------------------------------------------------

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
