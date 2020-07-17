#assignment_II
#Student ID:6201012610036

import random , pygame , math , time

width = 800
hight = 600
circlespeed = 5 
circlecolor=(255,255,255)
background=(0,0,0)

n = 10 #having blinking circle problem when having multiple circle
minrad = 10
maxrad = 20
c = []
i = 0
delete = False 
drawcircle = True

pygame.init()
screen = pygame.display.set_mode((width,hight))

#create circle class to keep track of every circle position
class circle():
    def __init__(self):
        self.r = random.randint(minrad,maxrad)
        self.x = random.randint(0+self.r,width-self.r)
        self.y = random.randint(0+self.r,hight-self.r)
        self.vx = random.randint((-1)*circlespeed,circlespeed)
        self.vy = random.randint((-1)*circlespeed,circlespeed)

    #draw a new circle 
    def draw(self):
        pygame.draw.circle(screen,circlecolor,(self.x,self.y),self.r)
    
    #moving positionof circle
    def updateposition(self):
        self.x += self.vx
        self.y += self.vy
    
    #checking the border impact
    def borderimpaccheck(self):
        if self.x-self.r <= 0 or self.x + self.r >= width:
            self.vx = (-1)*self.vx
            if self.x < 0: #line 43 - 46 using if circle getting bug out of the screen
                self.x = 1
            elif self.x > width: 
                self.x = width - 1

        if self.y-self.r <= 0 or self.y + self.r >= hight:
            self.vy = (-1)*self.vy
            if self.y < 0: #the same as line 43-46
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
    #check for colision while creating new circle
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
            if d != None:
                del c[d]
            time.sleep(0.03)
            d = None
    
    #border colision check
    for i in range(len(c)):
        c[i].updateposition()
        c[i].borderimpaccheck()
        #updating the screen and circle position
        for k in range(len(c)):
            c[k].draw()
        pygame.display.update()
        screen.fill(background)
        #colision between circle check
        for j in range(len(c)):
            if i != j:
                det = math.hypot(abs(c[j].x-c[i].x),abs(c[j].y-c[i].y))
                if det <= c[i].r+c[j].r:
                    #after colision react for circle 
                    #v1-------------------------------------
                    c[i].vx *= (-1)
                    c[i].vy *= (-1)
                
                    #v2 more random but can stick to other circle for a short time
                    #c[i].vx = random.randint((-1)*circlespeed,circlespeed)
                    #c[i].vy = random.randint((-1)*circlespeed,circlespeed)


