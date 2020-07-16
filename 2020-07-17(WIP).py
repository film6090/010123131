#assignment_II
#Student ID:6201012610036
import random , pygame , math , time

width = 800
hight = 600
pygame.init()
circlecolor=(255,255,255)
background=(0,0,0)
screen = pygame.display.set_mode((width,hight))

n = 5
c = []
i = 0
delete = False 
drawcircle = True

#create circle class to keep track of every circle position
class circle():
    def __init__(self):
        self.r = random.randint(10,20)
        self.x = random.randint(0+self.r,width-self.r)
        self.y = random.randint(0+self.r,hight-self.r)
        self.vx = random.randint(-5,5)
        self.vy = random.randint(-5,5)

    #draw a new circle 
    def draw(self):
        pygame.draw.circle(screen,circlecolor,(self.x,self.y),self.r)

    def updateposition(self):
        self.x = int(self.x+self.vx)
        self.y = int(self.y+self.vy)

    def borderimpaccheck(self):
        if self.x-self.r <= 0 or self.x + self.r >= width:
            self.vx = (-1)*self.vx
            if self.x < 0:
                self.x = 1
            elif self.x > width:
                self.x = width - 1

        if self.y-self.r <= 0 or self.y + self.r >= hight:
            self.vy = (-1)*self.vy
            if self.y < 0:
                self.y = 1
            elif self.y > width:
                self.y = width - 1
            

#------------------------------------------------------------------------------------------------------------
#create circle to a number of n
while len(c) < n :
    if i == 0:
        c.append(str(i))
        c[i] = circle()
        c[i].draw()
        i+=1
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
        i += 1
#-------------------------------------------------------------------------------------------------------   
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    #check the left mouse click and cursor position
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        x,y = pygame.mouse.get_pos()
        #check position for cursor if it inside circle or not
        for i in range(len(c)):
            rad = math.hypot(abs(x-c[i].x),abs(y-c[i].y))
            time.sleep(0.1)
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
            for k in range(len(c)):
                c[k].draw()
                pygame.display.update()

    for i in range(len(c)):
        screen.fill(background)
        for k in range(len(c)):
            c[k].draw()
            pygame.display.update()
        c[i].updateposition()
        c[i].borderimpaccheck()
        for j in range(len(c)):
            if i != j:
                det = math.hypot(abs(c[j].x-c[i].x),abs(c[j].y-c[i].y))
                if det <= c[i].r+c[j].r:
                    c[i].vx = (-1)*random.randint(0,5)
                    c[i].vy = (-1)*random.randint(0,5)
                    c[j].vx = (-1)*random.randint(0,5)
                    c[j].vy = (-1)*random.randint(0,5)
                
                     

