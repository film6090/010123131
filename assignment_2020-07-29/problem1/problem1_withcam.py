#this code dosen't get any test run for the reason that i didn't have any web camera this code may contain a lot of error.



import pygame , random , pygame.camera
#--------------------------------------------------------------------------------------------
#function

def changebg(M_pos,N_pos,color=(0,0,0)):
    for i in range(h):
        for j in range(w):
            surface.set_at((M_pos*w+j,N_pos*h+i),color)
            if color == (0,0,0):
                fill[N_pos][M_pos]=True
    screen.blit(surface,(0,0))
    pygame.display.update()

def blank():
    for i in range(M):
        for j in range(N):
            if fill[j][i] == False:
                return False
    return True

def open_camera( frame_size=(1280,720),mode='RGB'):
    pygame.camera.init()
    list_cameras = pygame.camera.list_cameras()
    if list_cameras:
        camera = pygame.camera.Camera(list_cameras[0], frame_size, mode )
        return camera 
    return None

def g_line()
    for i in range(M):
        for j in range(scr_w):
            surface.set_at((j,i*h),(0,255,0))

    for i in range(N):
        for j in range(scr_h):
            surface.set_at((i*w,j),(0,255,0))

    for i in range(scr_w):
        surface.set_at((i,scr_h-1),(0,255,0))

    for i in range(scr_w):
        surface.set_at((scr_w-1,i),(0,255,0))

#-----------------------------------------------------------------------------------------------------------
#setup

M,N = 5,5
scr_w , scr_h = 1280,720
pygame.init()
screen = pygame.display.set_mode( (scr_w, scr_h) )
#bg = pygame.image.load(r"c:\Users\Firn_Film\Desktop\film\.vscode\image.jpg").convert()
#scr_w , scr_h = bg.get_width() , bg.get_height()
#screen = pygame.display.set_mode( (scr_w, scr_h) )
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )
#screen.blit(bg,(0,0))
w = scr_w//M
h = scr_h//N
fill = [ [ False for i in range(M) ] for j in range(N) ]
camera = open_camera()
camera.start()
g_line()
screen.blit(surface,(0,0))
pygame.display.update()


#------------------------------------------------------------------------------------------

running = True
while running == True:
    img = camera.get_image()
    if img != None:
        for i in range(N):
            for j in range(M):
                if fill[i][j] == False:
                    screen.blit(img,(j*w,i*h),(j*w,i*h,w,h))
        pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        x,y = pygame.mouse.get_pos()
        changebg(x//w,y//h)
    if blank() == True:
        screen.blit(img,(0,0))
        pygame.display.update()
    
