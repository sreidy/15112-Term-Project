###########################################################
#MAZE GENERATION                                          #
# source: http://www.migapro.com/depth-first-search/      #
# Program uses recursive backtraking to fill in a         #
#Key:                                                     #
#0 = wall(not path)                                       #
#1 = path                                                 #
#2 = start                                                #
#3 = end                                                  #
# maze.                                                   #
###########################################################
import random
import math
from Tkinter import *

def make2dList(rows,cols,fill):
    return [ ([fill] * cols) for row in xrange(rows)]


def makeMaze(rows,cols):
    if rows % 2 == 0:
        maze = make2dList(rows,cols,0)
        currentCell = (len(maze)-1,len(maze[0])/2-1)
        maze[currentCell[0]][currentCell[1]] = 1
        recursiveMaze(maze, currentCell)
        # add exit location 
        exitRow = 0
        exitCol = cols / 2
        #marking the start       
        #check cell below it to find path
        while maze[0].count(1) == 0:
            if maze[exitRow+1][exitCol] == 1:
                maze[exitRow][exitCol] = 1
            else:
                exitCol+= 1
        return maze
    else:
        return  "must enter even number of rows"
        
def generateRandomDirs():
    dirs = ["North","South","East","West"]
    random.shuffle(dirs)
    return dirs

def recursiveMaze(maze, currentCell):
    dirs = generateRandomDirs()
    (rows, cols) = (len(maze), len(maze[0]))
    (row, col) = currentCell
    for i in xrange(4):
        if (dirs[i] == "North"):
            # Check up
            if (row - 2 <= 0): pass
            elif (maze[row-2][col] == 0):
                # Empty
                maze[row-2][col] = 1
                maze[row-1][col] = 1
                recursiveMaze(maze, (row-2, col))
        elif (dirs[i] == "South"):
            # check down
            if (row + 2 >= rows): pass
            elif (maze[row + 2][col]) == 0:
                maze[row + 2][col] = 1
                maze[row + 1][col] = 1
                recursiveMaze(maze, (row+2,col))
        elif (dirs[i] == "East"):
            # check Right
            if (col -2 <= 0): pass
            elif (maze[row][col - 2]) == 0:
                  maze[row][col -2] = 1
                  maze[row][col -1] = 1
                  recursiveMaze(maze, (row,col-2))
        elif (dirs[i] == "West"):
            # check Left
            if (col + 2 >= cols): pass
            elif (maze[row][col + 2]) == 0:
                  maze[row][col + 2] = 1
                  maze[row][col + 1] = 1
                  recursiveMaze(maze,(row,col +2))

def print2dList(maze):
    if (maze == []):
        # So we don't crash accessing a[0]
        print []
        return
    rows = len(maze)
    cols = len(maze[0])
    fieldWidth = maxItemLength(maze)
    print "[ ",
    for row in xrange(rows):
        if (row > 0): print "\n  ",
        print "[ ",
        for col in xrange(cols):
            if (col > 0): print ",",
            # The next 2 lines print a[row][col] with the given fieldWidth
            format = "%" + str(fieldWidth) + "s"
            print format % str(maze[row][col]),
        print "]",
    print "]"
    
def maxItemLength(a):
    maxLen = 0
    rows = len(a)
    cols = len(a[0])
    for row in xrange(rows):
        for col in xrange(cols):
            maxLen = max(maxLen, len(str(a[row][col])))
    return maxLen
# test for maze gerenation 
#print2dList(makeMaze(10,10))
###########################################################
#Test Draw Maze 
# Displays the maze from a the top. 
# may be implemented as map latter                        #
# Anmiation Class Source:                                 #
#http://www.kosbie.net/cmu/fall-13/15-112/                #
###########################################################

class TestAnimation(object):
    # Override these methods when creating your own animation
    def mousePressed(self, event): pass
    def keyPressed(self, event): pass
    def timerFired(self): pass
    def init(self): pass
    def redrawAll(self): pass
    
    # Call app.run(width,height) to get your app started
    def run(self):
        # create the root and the canvas
        root = Tk()
        self.cellSize = 8
        rows = self.rows
        cols = self.cols 
        cellSize = self.cellSize
        self.width = cols*cellSize
        self.height =   rows*cellSize
        self.canvas = Canvas(root, width=self.width, height=self.height)
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
        root.mainloop()  # This call BLOCKS 

class TestMaze(TestAnimation):
    
    def __init__(self,rows,cols):
        self.rows = rows
        self.cols = cols
        self.testMaze = makeMaze(rows,cols)
        
    def redrawAll(self):
        rows = self.rows
        cols = self.cols 
        testMaze = self.testMaze
        for row in xrange(rows):
            for col in xrange(cols):
                if testMaze[row][col] == 1:
                    self.drawTestMazeCell(row,col,"white")
                else:
                    self.drawTestMazeCell(row,col,"Black")
                    
    def drawTestMazeCell(self,row,col,color):
            cellSize = self.cellSize
            left =  col * cellSize
            right = left + cellSize
            top =  row * cellSize
            bottom = top + cellSize
            self.canvas.create_rectangle(left, top, right, bottom, fill=str(color))
#Test Here
# may be implemented as map latter          
#testMaze = TestMaze(100,100)
#testMaze.run()     

###########################################################
#Maze Game                                                #
# Anmiation Class Source:                                 #
#http://www.kosbie.net/cmu/fall-13/15-112/                #
###########################################################           
                    
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
# Location of tiles
#        
class Game(Animation):
    def __init__(self,rows,cols,canvasWidth = 720, canvasHeight = 576):
            #self.showBox =False
            #self.player = Player(canvasWidth, canvasHeight)
            #self.bindingBox = BindingBox(canvasWidth,canvasHeight)
            #self.walls = [Wall(100,100,150,500), Wall(500,100,550,500)]
            self.maze = Maze(rows,cols,canvasWidth,canvasHeight)
        # to be changed later in a function that randomly generates mazes

         
         
         
         
            
    def redrawAll(self):
        self.canvas.delete(ALL)
        self.maze.draw(self.canvas)
        #if self.showBox == True:
            #bindingBox.draw(canvas) 
        #self.player.draw(self.canvas)
    
    
    def timerFired(self):
        """
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
            """

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

class Maze(object):
    
    def __init__(self,rows,cols,canvasHeigth,canvasWidth):
        self.rows = rows
        self.cols = cols
        self.canvasHeigth = canvasHeigth 
        self.canvasWidth = canvasWidth 
        self.maze = makeMaze(rows,cols)
        self.maze = self.addMazeEvents()
        
    def addMazeEvents(self):
        rows = self.rows
        cols = self.cols 
        maze = self.maze
        self.startRow = rows
        self.startCol = cols / 2
        endRow = 0 
        endCol = maze[endRow].index(1)
        #maze[self.startRow][self.startCol] = ("start")
        #maze[endRow][endCol] = ("end")
        # to do: loop through each element in maze and and events to rooms
    
    def draw(self,canvas):
        canvasHeight = self.canvasHeigth 
        canvasWidth = self.canvasWidth 
        border = 15
        rows = self.rows
        cols = self.cols
        maze = self.maze
        for row in xrange(rows):
            for col in xrange(cols):
                left = (abs(col - self.startCol) * (-canvasWidth)) + border
                top =  (abs(row - self.startRow) * (-canvasHeight)) + border
                right =((abs(col- self.startCol) *(canvasWidth)) +canvasWidth +
                        border)
                bottom =((abs(row-self.startRow) *(canvasHeight))+canvasHeight+
                        border)
                print left,top,right,bottom
                if maze[row][col] == 0:
                    color = "Black"
                else:
                    color = "white"
                canvas.create_rectangle(left,top,right,bottom,fill = color)
                
                
                
        
    def move(self,dx,dy):
        pass
        
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
                                
            
        
        
        
        
                            
game = Game(8,8)
game.run()                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        


