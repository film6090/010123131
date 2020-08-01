import pygame , random , pygame.camera

#this version use 2 image and switch between it to simulate webcam and keep track of every swap section.

def open_camera( frame_size=(1280,720),mode='RGB'):
    pygame.camera.init()
    list_cameras = pygame.camera.list_cameras()
    if list_cameras:
        camera = pygame.camera.Camera(list_cameras[0], frame_size, mode )
        return camera 
    return None 

def swap(M_pos,N_pos,M_target,N_target,image):
    p1=pic[M_pos][N_pos]
    p2=pic[M_target][N_target]
    pic[M_pos][N_pos]=p2
    pic[M_target][N_target]=p1
    screen.blit(image,(M_pos*w,N_pos*h),((p2//M)*w,(p2%M)*h,w,h))
    screen.blit(image,(M_target*w,N_target*h),((p1//M)*w,(p1%M)*h,w,h))
    pygame.display.update()

refresh_rate = 75
M,N = 10,10
scr_w , scr_h = 500 , 500
pygame.init()
screen = pygame.display.set_mode( (scr_w, scr_h) )
bg_1 = pygame.image.load(r"image_1_path").convert()
bg_2 = pygame.image.load(r"image_2_path").convert()
scr_w , scr_h = bg_1.get_width() , bg_1.get_height()
screen = pygame.display.set_mode( (scr_w, scr_h) )
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )
screen.blit(bg_1,(0,0))
w = scr_w//M
h = scr_h//N
pygame.display.update()
pic = [[i+(j*M) for i in range(M)]for j in range(N)]
clock = pygame.time.Clock()
#camera = open_camera()
#camera.start()
r=0
drag = False
running = True
while running == True:
    clock.tick(refresh_rate)
    r+=1
    #img = camera.get_image()
    #if img != none:
    if (r//1000)%2 == 0:
        for i in range(N):
            for j in range(M):
                screen.blit(bg_1,(j*w,i*h),((pic[j][i]//M)*w,(pic[j][i]%M)*h,w,h))
    else:
        for i in range(N):
            for j in range(M):
                screen.blit(bg_2,(j*w,i*h),((pic[j][i]//M)*w,(pic[j][i]%M)*h,w,h))
    pygame.display.update()
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
            if c1!=c2 or r1!=r2:
                if (i//1000)%2 == 0:
                    swap(c1,r1,c2,r2,bg_1)
                else:
                    swap(c1,r1,c2,r2,bg_2)
                pygame.display.update()
            drag = False
    if r == 10000:
        r = 0    
        screen.fill((0,0,0))
        pygame.display.update()
