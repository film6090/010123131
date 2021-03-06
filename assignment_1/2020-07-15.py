#assignment_I
#Student ID:6201012610036
import random , pygame , math , time

pygame.init()
screen = pygame.display.set_mode((800,600))

n = 10
c = []
i = 0
delete = False 
drawcircle = True

#create circle class to keep track of every circle position
class circle():
    def __init__(self):
        self.r = random.randint(10,20)
        self.x = random.randint(0+self.r,800-self.r)
        self.y = random.randint(0+self.r,600-self.r)
#draw a new circle 
    def draw(self):
        pygame.draw.circle(screen,(255,255,255),(self.x,self.y),self.r)

#create circle to a number of n
while len(c) < n :
    if i == 0:
        c.append(str(i))
        c[i] = circle()
        c[i].draw()
        i+=1
        pygame.display.update()
    if drawcircle == True:
        c.append(str(i))
    c[i] = circle()
    drawcircle = True
    #check for colision
    for j in range(len(c)):
        if i != j:
            disp = math.hypot( c[j].x - c[i].x , c[j].y - c[i].y )
            if disp < ( c[j].r + c[i].r ):
                drawcircle = False
    #create circle if new circle dosen't overlap
    if drawcircle == True:
        c[i].draw()
        pygame.display.update()
        i += 1
   
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    #check the left mouse click and cursor position
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        x,y = pygame.mouse.get_pos()
        time.sleep(0.5)
        #check position for cursor if it inside circle or not
        for i in range(len(c)):
            rad = math.hypot(abs(x-c[i].x),abs(y-c[i].y))
            if rad < c[i].r:
                d = i
                delete = True
                #checking if the clicking circle is the biggest or not
                for j in range(len(c)):
                    if i != j:
                        if c[i].r < c[j].r :
                            delete = False
        #remove the biggest circle
        if delete == True:
            del c[d]
            screen.fill((0,0,0))
            for k in range(len(c)):
                c[k].draw()
            pygame.display.update()
