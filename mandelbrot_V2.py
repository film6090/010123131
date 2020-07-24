import threading
import pygame

N = 4 #number of thread useing to draw
scr_w, scr_h =1920,1080 #screen resolution
screen_ratio=[16,19]
scale = 0.01-scr_h/150000 #up or down scale of manderbrot depending on height
f = 20 #higher number = smaller area for thread to compute but more section
row=int((scr_h*f)/(screen_ratio[1]*100))
column=int((scr_w*f)/(screen_ratio[0]*100))
write_able=[ [ True for i in range(column) ] for j in range(row) ]
running_thread=[False for i in range(N)]
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
    global finish
    for i in range(column):
        for j in range(row):
            if write_able[i][j] == True:
                rowandcolumn = [i,j]
                return rowandcolumn
    Finish = True
    return False

color,r,g,b = 0,0,0,0
def thread_func(i,row_start,column_start,surface):
    global write_able,running_thread
    running_thread[i]=True
    write_able[row_start][column_start]=False
    for y in range(int(scr_h/row)):
        for x in range(int(scr_w/column)):
            color = mandelbrot(complex(scale*(column_start*int(scr_w/column)+x-scr_w/2) -0.55 ,scale*(row_start*int(scr_h/row)+y-scr_h/2) ))
            r = (color << 6) & 0xc0
            g = (color << 4) & 0xc0
            b = (color << 2) & 0xc0
            surface.set_at( (column_start*int(scr_w/column)+x,row_start*int(scr_h/row)+y), (255-r,255-g,255-b) )
        screen.blit( surface, (0,0) )
        pygame.display.update()
    running_thread[i]=False
    
for i in range(N):
    j=int(i/column)
    t = threading.Thread(target=thread_func, args=(i,j,i%column,surface))
    list_threads.append( t )

for t in list_threads:
    t.start()

running = True
while running:
    if finish != True:
        for i in range(len(running_thread)):
            if running_thread[i] == False:
                rc = findrowandcolumn()
                if rc!=False:
                    r=rc[0]
                    c=rc[1]
                    list_threads[i] = threading.Thread(target=thread_func,args=(i,r,c,surface))
                    list_threads[i].start()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()