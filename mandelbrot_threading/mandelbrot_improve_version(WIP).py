import threading
import pygame

N = 10 #number of thread useing to draw
scr_w, scr_h = 1600,900 
screen_ratio=[16,9]
fuequency=10
scale = 0.01-scr_h/120000 #up or down scale of manderbrot depending on height
row=int((scr_w/(screen_ratio[0]*100))*fuequency)
colmn=int((scr_h/(screen_ratio[1]*100)*fuequency)
write_able=[(true)*row]*column
running_thread=[False*N]
list_semaphores = [ threading.Semaphore(0) for i in range(N) ]
list_threads = []
finish =False

pygame.init()
screen = pygame.display.set_mode( (scr_w, scr_h) )
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )


def mandelbrot(c,max_iters=63):
    i = 0
    z = complex(0,0)
    while abs(z) <= 2 and i < max_iters:
        z = z*z + c
        i += 1 
    return i

def findrowandcolumn():
    for i in range(row):
        for j in range(colunm):
            if write_able[i][j] == True:
                rowandcolumn = [i,j]
                return rowandcolumn
    Finish = True

color,r,g,b = 0,0,0,0
def thread_func(id,row_start,column_start,surface):
    global write_able,running_thread
    running_thread[id]=True
    write_able[row_start][column_start]=False
    for y in range(int(scr_h/column)):
        for x in range(int(scr_w/row)):
            color = mandelbrot(complex(scale*(row_start*100+x-scr_w/2) -0.55 ,scale*(column_start*100+y-scr_h/2) ))
            r = (color << 6) & 0xc0
            g = (color << 4) & 0xc0
            b = (color << 2) & 0xc0
            surface.set_at( (row_start*100+x, column_start*100+y), (255-r,255-g,255-b) )
        screen.blit( surface, (0,0) )
        pygame.display.update()
    running_therad[id]=False
    
for i in range(N):
    j=int(i/row)
    t = threading.Thread(target=thread_func, args=(i,i%row,j,surface))
    list_threads.append( t )

for t in list_threads:
    t.start()

running = True
while running:
    if finish != True:
        for i in range(running_thread):
            if running_thread[i] == False:
                rc = findrowandcolumn
                list_thread[i] = threading.Thread(target=thread_function,args=(i,rc[0],rc[1],surface))
                list_thread[i].start()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
