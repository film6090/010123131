import pygame , random

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


M,N = 5,5

scr_w , scr_h = 500,500

pygame.init()
screen = pygame.display.set_mode( (scr_w, scr_h) )
bg = pygame.image.load(r"image_path").convert()
scr_w , scr_h = bg.get_width() , bg.get_height()
screen = pygame.display.set_mode( (scr_w, scr_h) )
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )
screen.blit(bg,(0,0))
w = scr_w//M
h = scr_h//N
fill = [ [ False for i in range(M) ] for j in range(N) ]


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

screen.blit(surface,(0,0))
pygame.display.update()

finish = False
running = True
while running == True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        x,y = pygame.mouse.get_pos()
        changebg(x//w,y//h)

    if blank() == True:
        screen.blit(bg,(0,0))
        pygame.display.update()
