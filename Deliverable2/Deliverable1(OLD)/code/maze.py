 # MAZE CODE

# Inital code for maze aspect of the project
# for final project the mazes will be randomly generated, and for testing their 
# will be a premade maze for testing. 
# the background of the maze will be a feed from a webcame to be added at a 
# latter time 


# Animation.py

import random
from Tkinter import *

###########################################
# Animation class
###########################################

class Animation(object):
    # Override these methods when creating your own animation
    def mousePressed(self, event): pass
    def keyPressed(self, event): pass
    def timerFired(self): pass
    def init(self): pass
    def redrawAll(self): pass
    
    # Call app.run(width,height) to get your app started
    def run(self, width=600, height=400):
        # create the root and the canvas
        root = Tk()
        self.width = width
        self.height = height
        self.canvas = Canvas(root, width=width, height=height)
        self.canvas.pack()
        # set up events
        def redrawAllWrapper():
            self.canvas.delete(ALL)
            self.redrawAll()
        def mousePressedWrapper(event):
            self.mousePressed(event)
            redrawAllWrapper()
        def keyPressedWrapper(event):
            self.keyPressed(event)
            redrawAllWrapper()
        root.bind("<Button-1>", mousePressedWrapper)
        root.bind("<Key>", keyPressedWrapper)
        # set up timerFired events
        self.timerFiredDelay = 250 # milliseconds
        def timerFiredWrapper():
            self.timerFired()
            redrawAllWrapper()
            # pause, then call timerFired again
            self.canvas.after(self.timerFiredDelay, timerFiredWrapper)
        # init and get timerFired running
        self.init()
        timerFiredWrapper()
        # and launch the app
        root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)
        
class Game(Animation):
    def __init__(self,canvasWidth = 600, canvasHeight = 400):
            self.showBox =False
            self.player = Player(canvasWidth, canvasHeight)
            self.bindingBox = BindingBox(canvasWidth,canvasHeight)
            self.walls = [Wall(100,100,150,500), Wall(500,100,550,500)]
            
        # to be changed later in a function that randomly generates mazes
                    
        
    def redrawAll(self):
        self.canvas.delete(ALL)
        if self.showBox == True:
            bindingBox.draw(canvas) 
        for item in self.walls:
            item.draw(self.canvas)
        self.player.draw(self.canvas)
    
    
    def timerFired(self):
        mazeMove = self.bindingBox.bindingBoxCollision(self.player)
        wallDx, wallDy = 0,0
        if mazeMove != None:
            if mazeMove == "up": wallDy = +2
            elif mazeMove == "down": wallDy = -2
            elif mazeMove == "right": wallDx = - 2
            elif mazeMove == "left" : wallDx = +2

        for item in self.walls:
            item.move(wallDx,wallDy)
            if self.player.playerCollision(item):
                print "aaaaaaa"
                # change to a gmae over state latter 

    def keyPressed(self,event):
        print "a"
        if event.keysym =="d":
            self.showBox = not self.showBox
        if event.keysym == "r":
            self.init()
        if event.keysym == "Up":
            self.player.move(0,-6)
        if event.keysym == "Left":
            self.player.move(-6,0)
        if event.keysym == "Right":
            self.player.move( 6,0)
        if event.keysym == "Down":
            self.player.move(0,6)
        self.redrawAll()

       
        
        """
        if event.keysym == "up":self.player.move(0,-2):
        elif event.keysym == "down":
            self.player.move(0 ,+2)
        elif event.keysym == "left":
            self.player.move(-2,0)
        elif event.keysym == "right":
            self.player.move(0,+2)
        elif event.keysym == "d":
            self.showBox = not self.showBox
            """

class Player(object):
    def __init__(self,canvasWidth,canvasHeight):
        self.playerX = canvasWidth / 2
        self.playerY = canvasHeight / 2
        self.radius = 20
        self.left = self.playerX - self.radius
        self.top = self.playerY - self.radius
        self.right = self.playerX + self.radius
        self.bottom = self.playerY + self.radius 
        
    def draw(self,canvas):
        canvas.create_oval(self.left, self.top,self.right,self.bottom,
                            fill = "orange")

    def move(self,dx,dy):
        self.playerX += dx
        self.playerY += dy
        
    def playerCollision(self,other):
              # points on a rectangle 
              #Cite: collsion code from HW10
        grace = 5
        (selfLeft, selfTop, selfRight, selfBottom) = (self.left,self.top,
                                                      self.right,self.bottom)
        (otherLeft,otherTop,otherRight, otherBottom) = (other.left,other.top,
                                                         other.right,
                                                         other.bottom)
        selfPoints = [(selfLeft, selfTop),(selfLeft, selfBottom),
                        (selfRight,selfBottom),(selfRight,selfTop)]
        otherPoints = [(otherLeft, otherTop),(otherLeft, otherBottom),
                        (otherRight,otherBottom),(otherRight,otherTop)]
        for i in xrange(len(otherPoints)):
            if (selfLeft - grace < otherPoints[i][0] < selfRight+grace and 
               selfTop-grace < otherPoints[i][1]< selfBottom+grace):
                print "a"
                return True  
        for i in xrange(len(selfPoints)):
            if (otherLeft < selfPoints[i][0] < otherRight and
               otherTop < selfPoints[i][1] < otherBottom): 
               print "b"
               return True 
        return False 
        
        
class BindingBox(object):
    def __init__(self,canvasWidth, canvasHeight):
        self.boxSize = 100 
        self.boxCx = canvasWidth / 2
        self.boxCy = canvasHeight / 2
        self.left = self.boxCx - self.boxSize
        self.top = self.boxCy - self.boxSize
        self.right = self.boxCx + self.boxSize
        self.bottom = self.boxCy + self.boxSize
        
            
    def draw(self,canvas):
        cx = self.boxCx
        cy = self.boxCy
        r = self.boxsize
        canvas.create_rectangle(cx -r,cy-r,cx+r,cy+r, fill = "red")
    
    def bindingBoxCollision(self, other):
        dirStr = None 
        if self.top >= other.top:
            dirStr = "up"
        elif self.left >= other.left:
            dirStr = "left"
        elif self.right <= other.right:
            dirStr = "right"
        elif self.bottom <= other.bottom:
            dirStr = "down"
        
        return dirStr
    
class Wall(object):
    
    def __init__(self,left,top,right,bottom,color= "cyan"):
        self.left = left
        self.right = right 
        self.top = top
        self.bottom = bottom 
        self.color = color
        
    def draw(self,canvas):
        canvas.create_rectangle(self.left,self.top,self.right,self.bottom,
                                fill = self.color)
                                
    def move(self,dx,dy):
        self.top += dy
        self.bottom += dy
        self.left += dx
        self.right += dx
                                
            
        
        
        
        
                            
game = Game()
game.run()