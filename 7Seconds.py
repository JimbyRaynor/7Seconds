import math
import sys
import random
from tkinter import *

sys.path.insert(0, "/home/deck/Documents")
import LEDlib

# TODO
# 7 second timer
# countdown to start
# animation list
# 2x flags
# 2x+1 flags
# pinball like? bouncers, speed increasers, ?
# moving walls/obsticles? -> moving away from original idea. Not a platformer


HitWall = False

def rotatepoints(points,angle,center):
         newpoints = []
         anglerad = math.radians(angle)
         cx,cy = center
         for x,y,z in points:
              x = x - cx
              y = y - cy
              newx = x* math.cos(anglerad)- y*math.sin(anglerad) + cx
              newy = x * math.sin(anglerad) + y*math.cos(anglerad) + cy
              newpoints.append((newx,newy,z))
         return newpoints


class LEDobj:
    def __init__(self, canvas,x=0,y=0,dx=0,dy=0, CharPoints = [], pixelsize = 2, typestring = "unknown"):
         self.x = x
         self.y = y
         self.dx = dx
         self.dy = dy
         self.canvas = canvas
         self.typestring = typestring
         self.LEDPoints = []
         self.OriginalCharPoints = CharPoints
         self.CharPoints = CharPoints.copy()
         self.collisionrect = (0,0,0,0)  # top left to bottom right
         self.collisionimage = 0
         self.collisionrectshow = False
         self.pixelsize = pixelsize
         LEDlib.psize = self.pixelsize
         LEDlib.createCharColourSolid(canvas,x,y,CharPoints,self.LEDPoints)
    def undraw(self):
         for p in self.LEDPoints:
            self.canvas.delete(p)
    def draw(self):
        self.undraw()
        self.LEDPoints = []  
        LEDlib.psize = self.pixelsize
        LEDlib.createCharColourSolid(self.canvas,self.x,self.y,self.CharPoints,self.LEDPoints)
        if self.collisionrectshow:
              canvas1.delete(self.collisionimage)
              self.showcollisionrect() 
    def move(self): 
         self.x = self.x + self.dx
         self.y = self.y + self.dy
         if self.x > MAXx-48: self.x = MAXx-48
         if self.y > MAXy-48: self.y = MAXy-48
         if self.x < 0 : self.x = 0
         if self.y < 0 : self.y = 0
         self.draw()
    def rotate(self,angledeg):
         centerx = sum(x for x,y,z in self.OriginalCharPoints)/len(self.OriginalCharPoints)
         centery = sum(y for x,y,z in self.OriginalCharPoints)/len(self.OriginalCharPoints)
         self.CharPoints = rotatepoints(self.OriginalCharPoints,angle=angledeg,center=(centerx,centery))
         self.draw()
    def showcollisionrect(self):
         self.collisionrectshow = True
         x1,y1,x2,y2 = self.collisionrect 
         self.collisionimage = canvas1.create_rectangle(self.x+x1,self.y+y1,self.x+x2,self.y+y2,fill="", outline = "white") 
         
class LEDscoreobj:
    def __init__(self, canvas,x=0,y=0, score = 0, colour = "white", pixelsize = 2, charwidth=23, numzeros = 0):
         self.x = x
         self.y = y
         self.score = score
         self.canvas = canvas
         self.LEDPoints = []
         self.colour = colour
         self.pixelsize = pixelsize
         self.charwidth = charwidth
         self.numzeros = numzeros 
         self.draw()
    def draw(self):
        LEDlib.charwidth = self.charwidth
        LEDlib.psize = self.pixelsize
        LEDlib.ShowColourScore(self.canvas,self.x,self.y,self.colour,self.score,self.LEDPoints, self.numzeros) 
    def undraw(self):
         for p in self.LEDPoints:
            self.canvas.delete(p)
    def update(self,myscore):
        self.score = myscore
        self.undraw()
        self.draw()





def checkcollisionrect(object1,object2):
     x1,y1,x2,y2 = object1.collisionrect 
     a1,b1,a2,b2 = object2.collisionrect
     x1 = x1 + object1.x
     y1 = y1 + object1.y
     x2 = x2 + object1.x
     y2 = y2 + object1.y 
     a1 = a1 + object2.x
     b1 = b1 + object2.y
     a2 = a2 + object2.x
     b2 = b2 + object2.y 
     if x2 < a1 or x1 > a2 or y2 < b1 or y1 > b2:
          return False
     else:
          return True


charRallyX = [(0,14,"#4C3A23"), (0,15,"#4C3A23"), (0,16,"#4C3A23"), (0,17,"#4C3A23"), (0,18,"#4C3A23"), (0,19,"#4C3A23"), (0,20,"#4C3A23"), (1,13,"#4C3A23"), (1,14,"#4C3A23"), (1,15,"#4C3A23"), (1,16,"#4C3A23"), (1,17,"#4C3A23"), (1,18,"#4C3A23"), (1,19,"#4C3A23"), (1,20,"#4C3A23"), (1,21,"#4C3A23"), (2,2,"#4C3A23"), (2,3,"#4C3A23"), (2,4,"#4C3A23"), (2,5,"#4C3A23"), (2,6,"#4C3A23"), (2,13,"#4C3A23"), (2,14,"#4C3A23"), (2,15,"#4C3A23"), (2,16,"#4C3A23"), (2,17,"#4C3A23"), (2,18,"#4C3A23"), (2,19,"#4C3A23"), (2,20,"#4C3A23"), (2,21,"#4C3A23"), (3,1,"#4C3A23"), (3,2,"#4C3A23"), (3,3,"#4C3A23"), (3,4,"#4C3A23"), (3,5,"#4C3A23"), (3,6,"#4C3A23"), (3,7,"#4C3A23"), (3,13,"#4C3A23"), (3,14,"#4C3A23"), (3,15,"#4C3A23"), (3,16,"#4C3A23"), (3,17,"#4C3A23"), (3,18,"#4C3A23"), (3,19,"#4C3A23"), (3,20,"#4C3A23"), (3,21,"#4C3A23"), (4,1,"#4C3A23"), (4,2,"#4C3A23"), (4,3,"#4C3A23"), (4,4,"#4C3A23"), (4,5,"#4C3A23"), (4,6,"#4C3A23"), (4,7,"#4C3A23"), (4,13,"#4C3A23"), (4,14,"#4C3A23"), (4,15,"#4C3A23"), (4,16,"#4C3A23"), (4,17,"#4C3A23"), (4,18,"#4C3A23"), (4,19,"#4C3A23"), (4,20,"#4C3A23"), (4,21,"#4C3A23"), (5,1,"#4C3A23"), (5,2,"#4C3A23"), (5,3,"#4C3A23"), (5,4,"#4C3A23"), (5,5,"#4C3A23"), (5,6,"#4C3A23"), (5,7,"#4C3A23"), (5,13,"#4C3A23"), (5,14,"#4C3A23"), (5,15,"#4C3A23"), (5,16,"#4C3A23"), (5,17,"#4C3A23"), (5,18,"#4C3A23"), (5,19,"#4C3A23"), (5,20,"#4C3A23"), (5,21,"#4C3A23"), (6,1,"#4C3A23"), (6,2,"#4C3A23"), (6,3,"#4C3A23"), (6,4,"#4C3A23"), (6,5,"#4C3A23"), (6,6,"#4C3A23"), (6,7,"#4C3A23"), (6,14,"#4C3A23"), (6,15,"#4C3A23"), (6,16,"#4C3A23"), (6,17,"#4C3A23"), (6,18,"#4C3A23"), (6,19,"#4C3A23"), (6,20,"#4C3A23"), (7,2,"#4C3A23"), (7,3,"#4C3A23"), (7,4,"#4C3A23"), (7,5,"#4C3A23"), (7,6,"#4C3A23"), (7,17,"#FFA07A"), (8,4,"#FFA07A"), (8,10,"#FFA07A"), (8,11,"#FFA07A"), (8,12,"#FFA07A"), (8,13,"#FFA07A"), (8,14,"#FFA07A"), (8,15,"#FFA07A"), (8,16,"#FFA07A"), (8,17,"#FFA07A"), (8,18,"#FFA07A"), (8,19,"#8B4513"), (8,20,"#8B4513"), (8,21,"#FF0000"), (8,22,"#FFFF00"), (8,23,"#FF0000"), (9,4,"#FFA07A"), (9,8,"#FFA07A"), (9,9,"#FFA07A"), (9,10,"#FFA07A"), (9,11,"#FFA07A"), (9,12,"#FFA07A"), (9,13,"#FFA07A"), (9,14,"#FFA07A"), (9,15,"#FFA07A"), (9,16,"#FFA07A"), (9,17,"#FFA07A"), (9,18,"#FFA07A"), (9,19,"#FFA07A"), (9,20,"#8B4513"), (9,21,"#8B4513"), (9,22,"#FF0000"), (9,23,"#FFFF00"), (10,1,"#FFA07A"), (10,2,"#FFA07A"), (10,3,"#FFA07A"), (10,4,"#FFA07A"), (10,5,"#FFA07A"), (10,6,"#FFA07A"), (10,7,"#FFA07A"), (10,8,"#FFA07A"), (10,9,"#FFA07A"), (10,10,"#FFA07A"), (10,11,"#AAAAAA"), (10,12,"#AAAAAA"), (10,13,"#AAAAAA"), (10,14,"#AAAAAA"), (10,15,"#AAAAAA"), (10,16,"#AAAAAA"), (10,17,"#FFA07A"), (10,18,"#FFA07A"), (10,19,"#FFA07A"), (10,20,"#FFA07A"), (11,0,"#FFA07A"), (11,1,"#FFA07A"), (11,2,"#FFA07A"), (11,3,"#FFA07A"), (11,4,"#FFA07A"), (11,5,"#FFA07A"), (11,6,"#FFA07A"), (11,7,"#FFA07A"), (11,8,"#FFA07A"), (11,9,"#FFA07A"), (11,10,"#AAAAAA"), (11,11,"#B5B3F5"), (11,12,"#FFFFFF"), (11,13,"#FFFFFF"), (11,14,"#FFFFFF"), (11,15,"#FFFFFF"), (11,16,"#B5B3F5"), (11,17,"#AAAAAA"), (11,18,"#FFA07A"), (11,19,"#FFA07A"), (11,20,"#FFA07A"), (12,0,"#FFA07A"), (12,1,"#FFA07A"), (12,2,"#FFA07A"), (12,3,"#FFA07A"), (12,4,"#FFA07A"), (12,5,"#FFA07A"), (12,6,"#FFA07A"), (12,7,"#FFA07A"), (12,8,"#FFA07A"), (12,9,"#FFA07A"), (12,10,"#AAAAAA"), (12,11,"#B5B3F5"), (12,12,"#FFFFFF"), (12,13,"#FFFFFF"), (12,14,"#FFFFFF"), (12,15,"#FFFFFF"), (12,16,"#B5B3F5"), (12,17,"#AAAAAA"), (12,18,"#FFA07A"), (12,19,"#FFA07A"), (12,20,"#FFA07A"), (13,1,"#FFA07A"), (13,2,"#FFA07A"), (13,3,"#FFA07A"), (13,4,"#FFA07A"), (13,5,"#FFA07A"), (13,6,"#FFA07A"), (13,7,"#FFA07A"), (13,8,"#FFA07A"), (13,9,"#FFA07A"), (13,10,"#FFA07A"), (13,11,"#AAAAAA"), (13,12,"#AAAAAA"), (13,13,"#AAAAAA"), (13,14,"#AAAAAA"), (13,15,"#AAAAAA"), (13,16,"#AAAAAA"), (13,17,"#FFA07A"), (13,18,"#FFA07A"), (13,19,"#FFA07A"), (13,20,"#FFA07A"), (14,4,"#FFA07A"), (14,8,"#FFA07A"), (14,9,"#FFA07A"), (14,10,"#FFA07A"), (14,11,"#FFA07A"), (14,12,"#FFA07A"), (14,13,"#FFA07A"), (14,14,"#FFA07A"), (14,15,"#FFA07A"), (14,16,"#FFA07A"), (14,17,"#FFA07A"), (14,18,"#FFA07A"), (14,19,"#FFA07A"), (14,20,"#8B4513"), (14,21,"#8B4513"), (14,22,"#FF0000"), (14,23,"#FFFF00"), (15,4,"#FFA07A"), (15,10,"#FFA07A"), (15,11,"#FFA07A"), (15,12,"#FFA07A"), (15,13,"#FFA07A"), (15,14,"#FFA07A"), (15,15,"#FFA07A"), (15,16,"#FFA07A"), (15,17,"#FFA07A"), (15,18,"#FFA07A"), (15,19,"#8B4513"), (15,20,"#8B4513"), (15,21,"#FF0000"), (15,22,"#FFFF00"), (15,23,"#FF0000"), (16,2,"#4C3A23"), (16,3,"#4C3A23"), (16,4,"#4C3A23"), (16,5,"#4C3A23"), (16,6,"#4C3A23"), (16,17,"#FFA07A"), (17,1,"#4C3A23"), (17,2,"#4C3A23"), (17,3,"#4C3A23"), (17,4,"#4C3A23"), (17,5,"#4C3A23"), (17,6,"#4C3A23"), (17,7,"#4C3A23"), (17,14,"#4C3A23"), (17,15,"#4C3A23"), (17,16,"#4C3A23"), (17,17,"#4C3A23"), (17,18,"#4C3A23"), (17,19,"#4C3A23"), (17,20,"#4C3A23"), (18,1,"#4C3A23"), (18,2,"#4C3A23"), (18,3,"#4C3A23"), (18,4,"#4C3A23"), (18,5,"#4C3A23"), (18,6,"#4C3A23"), (18,7,"#4C3A23"), (18,13,"#4C3A23"), (18,14,"#4C3A23"), (18,15,"#4C3A23"), (18,16,"#4C3A23"), (18,17,"#4C3A23"), (18,18,"#4C3A23"), (18,19,"#4C3A23"), (18,20,"#4C3A23"), (18,21,"#4C3A23"), (19,1,"#4C3A23"), (19,2,"#4C3A23"), (19,3,"#4C3A23"), (19,4,"#4C3A23"), (19,5,"#4C3A23"), (19,6,"#4C3A23"), (19,7,"#4C3A23"), (19,13,"#4C3A23"), (19,14,"#4C3A23"), (19,15,"#4C3A23"), (19,16,"#4C3A23"), (19,17,"#4C3A23"), (19,18,"#4C3A23"), (19,19,"#4C3A23"), (19,20,"#4C3A23"), (19,21,"#4C3A23"), (20,1,"#4C3A23"), (20,2,"#4C3A23"), (20,3,"#4C3A23"), (20,4,"#4C3A23"), (20,5,"#4C3A23"), (20,6,"#4C3A23"), (20,7,"#4C3A23"), (20,13,"#4C3A23"), (20,14,"#4C3A23"), (20,15,"#4C3A23"), (20,16,"#4C3A23"), (20,17,"#4C3A23"), (20,18,"#4C3A23"), (20,19,"#4C3A23"), (20,20,"#4C3A23"), (20,21,"#4C3A23"), (21,2,"#4C3A23"), (21,3,"#4C3A23"), (21,4,"#4C3A23"), (21,5,"#4C3A23"), (21,6,"#4C3A23"), (21,13,"#4C3A23"), (21,14,"#4C3A23"), (21,15,"#4C3A23"), (21,16,"#4C3A23"), (21,17,"#4C3A23"), (21,18,"#4C3A23"), (21,19,"#4C3A23"), (21,20,"#4C3A23"), (21,21,"#4C3A23"), (22,13,"#4C3A23"), (22,14,"#4C3A23"), (22,15,"#4C3A23"), (22,16,"#4C3A23"), (22,17,"#4C3A23"), (22,18,"#4C3A23"), (22,19,"#4C3A23"), (22,20,"#4C3A23"), (22,21,"#4C3A23"), (23,14,"#4C3A23"), (23,15,"#4C3A23"), (23,16,"#4C3A23"), (23,17,"#4C3A23"), (23,18,"#4C3A23"), (23,19,"#4C3A23"), (23,20,"#4C3A23")]
charPopsicle = [(0,1,"#8B4513"), (0,2,"#8B4513"), (0,3,"#8B4513"), (0,4,"#8B4513"), (0,5,"#8B4513"), (0,6,"#8B4513"), (0,7,"#8B4513"), (0,8,"#8B4513"), (0,9,"#8B4513"), (0,10,"#8B4513"), (0,11,"#8B4513"), (1,0,"#8B4513"), (1,1,"#8B4513"), (1,2,"#FFFFFF"), (1,3,"#FFFFFF"), (1,4,"#FFFFFF"), (1,5,"#8B4513"), (1,6,"#8B4513"), (1,7,"#8B4513"), (1,8,"#8B4513"), (1,9,"#8B4513"), (1,10,"#8B4513"), (1,11,"#FFFFFF"), (1,12,"#FFFFFF"), (2,0,"#8B4513"), (2,1,"#8B4513"), (2,2,"#8B4513"), (2,3,"#8B4513"), (2,4,"#8B4513"), (2,5,"#8B4513"), (2,6,"#8B4513"), (2,7,"#8B4513"), (2,8,"#8B4513"), (2,9,"#8B4513"), (2,10,"#8B4513"), (2,11,"#8B4513"), (2,12,"#FFFFFF"), (3,0,"#8B4513"), (3,1,"#8B4513"), (3,2,"#8B4513"), (3,3,"#8B4513"), (3,4,"#8B4513"), (3,5,"#8B4513"), (3,6,"#8B4513"), (3,7,"#8B4513"), (3,8,"#8B4513"), (3,9,"#8B4513"), (3,10,"#8B4513"), (3,11,"#FFFFFF"), (3,12,"#FFFFFF"), (3,13,"#C19153"), (3,14,"#C19153"), (3,15,"#C19153"), (3,16,"#C19153"), (3,17,"#C19153"), (4,0,"#8B4513"), (4,1,"#8B4513"), (4,2,"#8B4513"), (4,3,"#8B4513"), (4,4,"#8B4513"), (4,5,"#8B4513"), (4,6,"#8B4513"), (4,7,"#8B4513"), (4,8,"#8B4513"), (4,9,"#8B4513"), (4,10,"#8B4513"), (4,11,"#8B4513"), (4,12,"#FFFFFF"), (4,13,"#C19153"), (4,14,"#C19153"), (4,15,"#C19153"), (4,16,"#C19153"), (4,17,"#C19153"), (5,0,"#8B4513"), (5,1,"#8B4513"), (5,2,"#8B4513"), (5,3,"#8B4513"), (5,4,"#8B4513"), (5,5,"#8B4513"), (5,6,"#8B4513"), (5,7,"#8B4513"), (5,8,"#8B4513"), (5,9,"#8B4513"), (5,10,"#8B4513"), (5,11,"#8B4513"), (5,12,"#FFFFFF"), (6,0,"#8B4513"), (6,1,"#8B4513"), (6,2,"#8B4513"), (6,3,"#8B4513"), (6,4,"#8B4513"), (6,5,"#8B4513"), (6,6,"#8B4513"), (6,7,"#8B4513"), (6,8,"#8B4513"), (6,9,"#8B4513"), (6,10,"#8B4513"), (6,11,"#FFFFFF"), (6,12,"#FFFFFF"), (7,1,"#8B4513"), (7,2,"#8B4513"), (7,3,"#8B4513"), (7,4,"#8B4513"), (7,5,"#8B4513"), (7,6,"#8B4513"), (7,7,"#8B4513"), (7,8,"#8B4513"), (7,9,"#8B4513"), (7,10,"#8B4513"), (7,11,"#8B4513")]
charRobotron = [(1,4,"#FF0000"), (1,5,"#FFFF00"), (1,6,"#FFFF00"), (1,7,"#FFFF00"), (2,4,"#FF0000"), (2,5,"#FF0000"), (2,11,"#FFFF00"), (3,1,"#90EE90"), (3,2,"#00FFFF"), (3,4,"#FFFFFF"), (3,5,"#FF0000"), (3,6,"#FF0000"), (3,9,"#FF0000"), (3,10,"#FF0000"), (3,11,"#FFFF00"), (4,0,"#FF0000"), (4,1,"#90EE90"), (4,2,"#00FFFF"), (4,3,"#FF0000"), (4,4,"#FF0000"), (4,5,"#FFFFFF"), (4,6,"#FF0000"), (4,7,"#FF0000"), (4,8,"#FF0000"), (4,9,"#FF0000"), (4,10,"#FF0000"), (4,11,"#FFFF00"), (5,0,"#FF0000"), (5,1,"#90EE90"), (5,2,"#00FFFF"), (5,3,"#FF0000"), (5,4,"#FF0000"), (5,5,"#FFFFFF"), (5,6,"#FFFFFF"), (5,7,"#FF0000"), (5,8,"#FF0000"), (6,0,"#FF0000"), (6,1,"#90EE90"), (6,2,"#00FFFF"), (6,3,"#FF0000"), (6,4,"#FF0000"), (6,5,"#FFFFFF"), (6,6,"#FF0000"), (6,7,"#FF0000"), (6,8,"#FF0000"), (6,9,"#FF0000"), (6,10,"#FF0000"), (6,11,"#FFFF00"), (7,1,"#90EE90"), (7,2,"#00FFFF"), (7,4,"#FFFFFF"), (7,5,"#FF0000"), (7,6,"#FF0000"), (7,9,"#FF0000"), (7,10,"#FF0000"), (7,11,"#FFFF00"), (8,4,"#FF0000"), (8,5,"#FF0000"), (8,11,"#FFFF00"), (9,4,"#FF0000"), (9,5,"#FFFF00"), (9,6,"#FFFF00"), (9,7,"#FFFF00")]



STEPD = 4 # speed of car. This changes dx,dy.

mainwin = Tk()

MAXx = 700
MAXy = 400

score = 0

ShowAllCollisions = False

mainwin.geometry(str(MAXx)+"x"+str(MAXy)) 
canvas1 = Canvas(mainwin,width=MAXx,height= MAXy,bg="black")
canvas1.place(x=0,y=0)

myship = LEDobj(canvas1,300,30,dx = 0,dy = 0,CharPoints=charRallyX, pixelsize = 2,typestring = "car")
myship.collisionrect = (4,3,44,45)
if ShowAllCollisions: myship.showcollisionrect()

fruitlist = []
solidlist = []


for i in range(20):
     x = random.randint(0,600)
     y = 100+random.randint(0,200)
     if random.randint(0,2) > 0:
       fruit = LEDobj(canvas1,x,y,dx = 0,dy = 0,CharPoints=charPopsicle, pixelsize = 2,typestring = "fruit")
       fruit.collisionrect = (0,0,16,36)
       if ShowAllCollisions: fruit.showcollisionrect()
       fruitlist.append(fruit)
     else:
       robotron = LEDobj(canvas1,x,y,dx = 0,dy = 0,CharPoints=charRobotron, pixelsize = 2,typestring = "solid")
       robotron.collisionrect = (4,1,17,24)
       if ShowAllCollisions: robotron.showcollisionrect()
       solidlist.append(robotron)

displayscore = LEDscoreobj(canvas1,x=MAXx-200,y=20,score=0,colour="white",pixelsize=3, charwidth = 24,numzeros=8)

def gameloop():
    global HitWall, score
    myship.move()
    for fruit in fruitlist:
       if checkcollisionrect(myship,fruit): 
            LEDscoreobj(canvas1,x=fruit.x-14,y=fruit.y+10,score=100,colour="white",pixelsize=2, charwidth = 12)
            fruit.undraw()
            fruitlist.remove(fruit)
            score = score + 100
            displayscore.update(score)
    for solid in solidlist:
         if checkcollisionrect(myship,solid): 
            #myship.dx = -myship.dx
            #myship.dy = -myship.dy
            if not HitWall:
              myship.x = myship.x - myship.dx
              myship.y = myship.y - myship.dy
            myship.dx = 0
            myship.dy = 0
            HitWall = True
            break # exit the for loop
    mainwin.after(10,gameloop)

gameloop()

def mykey(event):
    global HitWall
    key = event.keysym
    if HitWall:
         HitWall = False
    elif   key == "w":
         myship.rotate(0)
         myship.dy = -STEPD
         myship.dx = 0
    elif key == "d":
         myship.rotate(90)
         myship.dy = 0
         myship.dx = STEPD
    elif key == "a":
         myship.rotate(270)
         myship.dy = 0
         myship.dx = -STEPD
    elif key == "s":
         myship.rotate(180)
         myship.dy = STEPD
         myship.dx = 0


mainwin.bind("<KeyPress>", mykey)
mainwin.mainloop()