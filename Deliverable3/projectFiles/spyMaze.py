###########################################################
#MAZE GENERATION                                          #
# source: http://www.migapro.com/depth-first-search/      #
# Program uses recursive backtraking to fill in a         #
#Key:                                                     #
#0 = wall(not path)                                       #
#1 = path                                                 #                                               
# maze.                                                   #
###########################################################
import random
import math
from Tkinter import *


def make2dList(rows,cols,fill):
    return [ ([fill] * cols) for row in xrange(rows)]
    
def index2dList(list,item):
    rows = len(list)
    cols = len(list[0])
    for row in xrange(rows):
        for col in xrange(cols):
            if list[row][col] == item:
                return (row,col)
    return None
        


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
        def motionMouseWrapper(event):
            self.motionMouse(event)
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
        # init and get timerFiwwwwwww
class TestMaze(TestAnimation):
    
    def __init__(self,rows,cols):
        self.rows = rows
        self.cols = cols
        self.maze = self.initMaze(makeMaze(rows,cols))
        
    def initMaze(self,maze):
        startRow = self.rows -1 
        startCol = len(maze[0])/2-1
        maze[startRow][startCol] = 2
        endRow = 0
        endCol = maze[endRow].index(1) 
        maze[endRow][endCol] = 3 
        return maze 

    def redrawAll(self):
        rows = self.rows
        cols = self.cols 
        maze = self.maze
        for row in xrange(rows):
            for col in xrange(cols):
                if maze[row][col] ==1:
                    self.drawTestMazeCell(row,col,"white")
                elif maze[row][col] == 2:
                    self.drawTestMazeCell(row,col,"green")
                elif maze[row][col] == 3:
                    self.drawTestMazeCell(row,col,"red")
                else:
                    self.drawTestMazeCell(row,col,"Black")
                    sssssssss
    def drawTestMazeCell(self,row,col,color):
            cellSize = self.cellSize
            left =  col * cellSize
            right = left + cellSize
            top =  row * cellSize
            bottom = top + cellSize
            self.canvas.create_rectangle(left, top, right, bottom, fill=str(color))
#Test Here
# may be implemented as map latter          
#testMaze = TestMaze(10,10)
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
    def run(self, width=720, height=576):
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
        def motionMouseWrapper(event):
            self.motionMouse(event)
            redrawAllWrapper()
        def keyPressedWrapper(event):
            self.keyPressed(event)
            redrawAllWrapper()
        def keyReleasedWrapper(event):
            self.keyReleased(event)
            redrawAllWrapper()
            
        def keyPushWrapper(event):
            self.keyPush(event)
            redrawAllWrapper()
        root.bind("<Button-1>", mousePressedWrapper)
        root.bind("<KeyPress>", keyPressedWrapper)
        self.canvas.bind("<Motion>", motionMouseWrapper)
        root.bind("<KeyRelease>",keyReleasedWrapper)
        # set up timerFired events
        self.timerFiredDelay = 25 # milliseconds
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
    def __init__(self,rows,cols,canvasHeight=576,canvasWidth=720):
        self.maze = Maze(rows,cols,canvasHeight,canvasWidth)
        self.rows = rows
        self.cols = cols 
        self.canvasHeight = canvasHeight
        self.canvasWidth = canvasWidth
        self.wallSize = 50 
        self.curentCel = None
        self.player = Player(canvasHeight,canvasWidth,self.maze,self.wallSize)
        self.gameOver = False
        self.hp = 100 
        self.mouseMoveX = canvasWidth / 2 
        self.mouseMoveY = canvasHeight / 2 - 30 
        self.pressedKeys = []
        self.projectiles =[]
        self.enemyShots = None
        self.event  = self.initEvents(rows,cols,canvasHeight, canvasWidth)
        self.invotory = Invotory(canvasHeight,canvasWidth)
        self.showHelp = False
        
    def initEvents(self,rows,cols,canvasHeight,canvasWidth):
        eventList = []
        #eventType = [enemy, tree, fire, pit,]
        self.curentEventRow = rows -1
        self.curentEventCol = (cols / 2) -1
        for row in xrange(rows):
            colList =[]
            for col in xrange(cols):
                events = []
                for item in xrange(12):
                    itemtype = random.randint(0,5)
                    if itemtype == 0: element = Enemy(canvasHeight,canvasWidth)
                    elif itemtype == 1: element = Enemy(canvasHeight,canvasWidth)
                    elif itemtype == 2: element = Tree(canvasHeight,canvasWidth)
                    elif itemtype == 3: element = Tree(canvasHeight,canvasWidth)
                    elif itemtype == 4: element = Tree(canvasHeight,canvasWidth)
                    elif itemtype == 5: element = Helth(canvasHeight,canvasWidth)
                    events.append(element)
                colList.append(events)
            eventList.append(colList)
        eventList[self.curentEventRow][self.curentEventCol] = []
        return eventList
                    
            

        
        
    
    def mousePressed(self, event):
        playerPos = self.player.playerLocation()
        self.projectiles.append(Wepon(playerPos[0],playerPos[1],
                                        playerPos[2],self.mouseMoveX, 
                                        self.mouseMoveY))
        
       
            
    def motionMouse(self,event):
        self.mouseMoveX, self.mouseMoveY = event.x,event.y

    
    def keyPressed(self, event):     
        if(len(event.keysym)) == 1 and event.keysym.isalpha():
            if event.keysym not in self.pressedKeys:
                self.pressedKeys.append(event.keysym)

                
    def keyReleased(self,event):
        if(len(event.keysym)) == 1 and event.keysym.isalpha():
            if event.keysym in self.pressedKeys:
                self.pressedKeys.remove(event.keysym)
           
        

    def timerFired(self): 
        self.walls = self.maze.findWalls()
        move = self.player.atWall(self.walls)
        self.playerMove()
        if self.maze.isGameOver():
            self.gameOver = True
            self.overState = "win"
        if move != None:
            self.projectiles =[]
            self.enemyShots = []
            self.maze.moveCell(move)
            if move == "north":self.curentEventRow += -1
            elif move == "south" : self.curentEventRow += 1
            elif move == "east" : self.curentEventCol += 1
            elif move == "west" : self.curentEventCol += -1
        curentEvent = self.event[self.curentEventRow][self.curentEventCol]
        for enemy in curentEvent:
            if enemy.enemyShots() != None: 
                self.enemyShots.append(enemy.enemyShots())
        for wepon in self.projectiles:
            for enemy in curentEvent:
                if wepon.collsion(enemy):
                    enemy.kill()
        if self.enemyShots != None:
            for shotList in self.enemyShots:
                for shot in shotList:
                    if shot.collsion(self.player):
                        self.hp += -0.5
        for event in curentEvent:
            test = self.player.collsion(event)
            if test:
                if event.isHealth():
                    if self.hp <= 100:
                        self.hp += 10
                    self.event[self.curentEventRow][self.curentEventCol].remove(event)
                    
                elif event.isTree():
                    self.hp += 0
                else:
                    self.hp += -0.5
        if self.hp <= 0:
            self.gameOver = True 
            self.overState = "lose"
            self.player.kill()
        self.redrawAll()
        
    def playerMove(self):
        pressedKeys = self.pressedKeys  
        if pressedKeys == []:
            self.showHelp = False           
        for key in pressedKeys:
            
            self.player.move(key)
            if key == "h": self.showHelp = True
            else: self.showHelp = False
    def redrawAll(self): 
        if self.gameOver != True:
            self.canvas.delete(ALL)
            self.maze.draw(self.canvas,self.wallSize)
            self.player.draw(self.canvas)
            playerLocation = self.player.playerLocation()
            curentEvent = self.event[self.curentEventRow][self.curentEventCol]
            for event in curentEvent:
                event.draw(self.canvas,playerLocation[0],playerLocation[1],
                                playerLocation[2])
            for wepon in self.projectiles:
                wepon.draw(self.canvas)
            if self.enemyShots != None:
                for shotList in self.enemyShots:
                    for shot in shotList:
                        shot.draw(self.canvas)
            self.invotory.drawLife(self.canvas,self.hp)
            if self.showHelp:
                drawHelp(self.canvas)
            self.player.drawCosshairs(self.canvas, self.mouseMoveX,self.mouseMoveY)
        else:
            self.drawGameOver()
            
        
            
    def drawGameOver(self):
        self.canvas.create_rectangle(0,0,self.canvasWidth,self.canvasHeight,
                                        fill = "black")
        if self.overState == "lose":
            text1 = "You have Lost"
            text2 = " Try Again"
            text3 = "close window and start new game" 
            self.canvas.create_text(self.canvasWidth/2, self.canvasHeight/2, 
                                text = text1,fill = "red", font = ("impact", 30, "bold"))
            self.canvas.create_text(self.canvasWidth/2,self.canvasHeight/2 + 50,
                                    text = text2 ,fill = "red",font = ("impact", 30, "bold"))
            self.canvas.create_text(self.canvasWidth / 2, self.canvasHeight / 2 + 90,
                                    text = text3 , fill = "red" , font = ("impact",15,"bold"))
                                
                                
        else:
            self.drawWin()
            
    def drawWin(self):
            text1 =" You have reached the End"
            text2 = "Victory is yours"
            text3 = "Try Again?"
            text4 = "close window and start a new game" 
            self.canvas.create_text(self.canvasWidth/2, self.canvasHeight/2-50, 
                                text = text1,fill = "red", font = ("impact", 30, "bold"))
            self.canvas.create_text(self.canvasWidth/2, self.canvasHeight/2, 
                                text = text2,fill = "red", font = ("impact", 30, "bold"))
            self.canvas.create_text(self.canvasWidth/2, self.canvasHeight/2+50, 
                                text = text3,fill = "red", font = ("impact", 30, "bold"))
            self.canvas.create_text(self.canvasWidth / 2, self.canvasHeight / 2 + 100,
                                    text = text4 , fill = "red",  font = ("impact",15,"bold"))
                                
    

        

class Maze(object):
    
    def __init__(self,rows,cols,canvasHeight,canvasWidth):
        self.rows = rows
        self.cols = cols
        self.canvasHeight= canvasHeight 
        self.canvasWidth = canvasWidth 
        self.maze = self.initMaze(makeMaze(rows,cols))
        self.gameOver = False



        
    def initMaze(self,maze):
        startRow = self.rows -1 
        startCol = len(maze[0])/2-1
        maze[startRow][startCol] = "player"
        endRow = 0
        endCol = maze[endRow].index(1) 
        maze[endRow][endCol] = "end"
        return maze 
    
    def moveCell(self,dir):
        playerRow = self.playerLocation[0]
        playerCol = self.playerLocation[1]
        walls = self.findWalls()
        if dir not in walls:
            if dir == "north":
                dRow = -1
                dCol = 0
            elif dir == "south":
                dRow = 1
                dCol = 0
            elif dir == "west":
                dRow = 0
                dCol = -1
            elif dir == "east":
                dRow = 0
                dCol = 1
            self.maze[playerRow][playerCol]= 1
            if self.maze[playerRow+dRow][playerCol+dCol] == "end":
                    print "you win"
                    self.gameOver = True 
            self.maze[playerRow+dRow][playerCol+dCol] = "player"
        
        
    def draw(self,canvas,wallSize =50 ):
        walls = self.findWalls()
        canvas.create_rectangle(0,0,self.canvasWidth,self.canvasHeight,fill ="white")
        self.drawCorner(canvas,wallSize)
        for wall in xrange(len(walls)):
            if walls[wall] == "north":
                left,top,right,bottom = (0,0,self.canvasWidth, wallSize)
            elif walls[wall] == "south":
                left,top,right,bottom = (0,(self.canvasHeight - wallSize),
                                        (self.canvasWidth),(self.canvasHeight))
            elif walls[wall] == "west":
                left,top,right,bottom = (0,0,wallSize,self.canvasHeight)
            elif walls[wall] == "east":
                left,top,right,bottom = ((self.canvasWidth - wallSize),0,
                                         self.canvasWidth, self.canvasHeight)
            canvas.create_rectangle(left,top,right,bottom,fill ="black")
        
    def findWalls(self):
        maze = self.maze
        playerLocation = index2dList(self.maze,"player")
        self.playerLocation = playerLocation 
        startRow= playerLocation[0]
        startCol= playerLocation[1]
        dirs = [(-1,0),(+1,0),(0,+1),(0,-1)]
        dirName = [ "north","south","east","west"]
        rows = self.rows
        cols = self.cols
        wallList = []
        for dir in xrange(len(dirs)):
            (drow,dcol) = dirs[dir]
            newRow = startRow + drow
            newCol = startCol + dcol
            if ((newRow < 0)or(newRow >= rows)or(newCol < 0)or(newCol >= cols) 
                or maze[newRow][newCol] == 0 ):
                wallList.append(dirName[dir])

        return wallList

    def drawCorner(self,canvas,wallSize = 50):
        canvas.create_rectangle(0,0,wallSize,wallSize,fill = "black")
        canvas.create_rectangle(self.canvasWidth -wallSize,0,self.canvasWidth,
                                wallSize,fill = "black")
        canvas.create_rectangle(0,self.canvasHeight - wallSize,wallSize,
                                self.canvasHeight,fill ="black")
        canvas.create_rectangle(self.canvasWidth -wallSize,
                                self.canvasHeight -wallSize,self.canvasWidth,
                                self.canvasHeight,fill ="black")
                                
    def isGameOver(self):
        return self.gameOver 
        
def drawHuman(canvas,Cx,Cy ,nType = "enemy"):
    headR = 10
    bodyWidth = 10
    legWidth = 5
    headcolor = "black"
    if nType == "player":
        headcolor = "red"
    canvas.create_oval(Cx - headR, (Cy - 30) - headR,
                        Cx + headR, (Cy - 30) + headR, fill = headcolor)
    canvas.create_rectangle( Cx - bodyWidth, (Cy - 20),
                            Cx + bodyWidth, (Cy+20) , 
                            fill = "black")
    canvas.create_rectangle(Cx - bodyWidth, (Cy+20) ,
                            Cx - bodyWidth + legWidth, Cy+ 40, fill="black")
    canvas.create_rectangle(Cx + bodyWidth - legWidth, Cy+ 20 ,
                            Cx + bodyWidth, Cy + 40, fill = "black")
                            
def bloodSpray(canvas,Cx,Cy):
    dx = 1
    startY = Cy
    for line in xrange(100):
        if line < 50 and line % 2 == 0: dy = random.randint(-5,-1)
        elif line < 50 and line % 2 != 0: dy = -1.5
        elif line >50 and line % 2 == 0: dy = random.randint(1,5)
        elif line > 50 and line % 2 != 0: dy = 1
        Cx += dx
        Cy += dy
        canvas.create_line(Cx,startY,Cx,Cy, fill = "red")
        
 
    
class Actor(object):
        def __init__(self,canvasHeight,canvasWidth,maze):
            self.canvasHeight = canvasHeight
            self.canvasWidth = canvasWidth
            
            
        
        def collsion(self,other):

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
                if (selfLeft  <= otherPoints[i][0] <= selfRight and 
                selfTop <= otherPoints[i][1]<= selfBottom):

                    return True 
            for i in xrange(len(selfPoints)):
                if (otherLeft <= selfPoints[i][0] <= otherRight and
                otherTop <= selfPoints[i][1] <= otherBottom): 
                    return True
            
            return False
        def move(self,v1,v2,v3,v4):
            pass
            
        def isHealth(self):
            return False
            
        def enemyShots(self):
            return None
        def isTree(self):
            return False
         
        def kill(self):
            pass
        
class Player(Actor):
    def __init__(self,canvasHeight,canvasWidth,maze,wallSize):
        self.canvasHeight = canvasHeight
        self.canvasWidth = canvasWidth
        self.Cx = canvasWidth / 2
        self.Cy = canvasHeight / 2
        self.R = 20 
        self.wallSize = wallSize 
        self.maze = maze
        self.dead = False
    def draw(self,canvas):
        r = self.R
        cx = self.Cx
        cy = self.Cy
        if self.dead == False:
            drawHuman(canvas,cx,cy,"player")
        else:
            bloodSpray(canvas,cx,cy)
        #canvas.create_oval(cx -r,cy-r,cx+r,cy+r,fill = "black")
        self.left = self.Cx - self.R
        self.right = self.Cx + self.R
        self.top = self.Cy - self.R
        self.bottom = self.Cy + self.R
      
        
    def move(self,dir):
        if self.dead == False:
            walls = self.walls 
            if dir == "w":
                border = 0
                if "north" in walls:
                    border = self.wallSize 
                if self.Cy -self.R <= border:
                    self.Cy += 0
                else:     
                    self.Cy += -6
            elif dir == "s":
                border = self.canvasHeight 
                if "south" in walls:
                    border = self.canvasHeight - self.wallSize
                if self.Cy + self.R >= border:
                    self.Cy += 0
                else:
                    self.Cy += 6
            elif dir == "d":
                border = self.canvasWidth
                if "east" in walls:
                    border = self.canvasWidth - self.wallSize 
                if self.Cx + self.R >= border:
                    self.Cx += 0
                else:
                    self.Cx +=6
            elif dir =="a":
                border = 0
                if "west" in walls:
                    border = self.wallSize
                if self.Cx - self.R <= border:
                    self.Cx += 0
                else:
                    self.Cx += -6
            
    def atWall(self,walls):
        width = self.canvasWidth
        height = self.canvasHeight
        self.walls = walls 
        gap = 4
        if "north" not in walls and (self.Cy - self.R) <= 0 :
            self.Cy = height - self.R - gap
            return "north"
        elif "south" not in walls  and (self.Cy + self.R) >= height:
            self.Cy = 0 + self.R + gap 
            return "south"
        elif "west" not in walls and (self.Cx -self.R) <= 0:
            self.Cx = width - self.R - gap
            return "west"
        elif "east" not in walls and (self.Cx + self.R) >= width:
            self.Cx = 0 + self.R + gap 
            return "east"
        else:
            return None

    def drawCosshairs(self,canvas,mouseX,mouseY):
        lineLen = 20
        cx = mouseX
        cy = mouseY
        canvas.create_line( cx,cy - lineLen,cx, cy +lineLen, width = 3,
                                fill = "red")
        canvas.create_line(cx - lineLen,cy,cx + lineLen,cy,width = 3, 
                                fill =  "red") 
    def playerLocation(self):
        return (self.Cx,self.Cy,self.R)
        
    def kill(self):
        self.dead = True
        
                    

class Wepon(Actor):
    def __init__(self,Cx,Cy,R,crossX, crossY):
        self.Cx = Cx
        self.Cy = Cy
        self.R = 8
        self.crossX = crossX
        self.crossY = crossY
        self.projectX = Cx
        self.projectY = Cy
        self.dx = float((crossX - Cx) / 30)
        self.dy = float((crossY - Cy) / 30)
        self.left = self.Cx - self.R
        self.right = self.Cx + self.R
        self.top = self.Cy - self.R
        self.bottom = self.Cy + self.R
        

        
    def draw(self,canvas):
        if self.dx != 0.0 and self.dy != 0.0:
            canvas.create_oval(self.projectX - self.R , self.projectY - self.R,
                                self.projectX + self.R, self.projectY + self.R,
                                fill = "black")
        self.projectX += self.dx
        self.projectY += self.dy 
        self.left = self.projectX - self.R
        self.right = self.projectX + self.R
        self.top = self.projectY - self.R
        self.bottom = self.projectY + self.R
        
        

class Enemy(Actor):
    def __init__(self,canvasHeight,canvasWidth):
        self.canvasHeigh = canvasHeight
        self.canvasWidth = canvasWidth
        self.Cx = random.randint(200,canvasHeight-50)
        self.Cy = random.randint(100,canvasWidth -100)
        self.R = 20
        self.dead = False
        self.left = self.Cx - self.R
        self.right = self.Cx + self.R
        self.top = self.Cy - self.R
        self.bottom = self.Cy + self.R
        
        
    def draw(self,canvas,playerX,playerY,playerR):
        if self.dead == False:
            if self.Cx < playerX: self.dx =1
            else: self.dx = -1
            if self.Cy < playerY : self.dy = 1
            else: self.dy = -1
            self.Cx += self.dx 
            self.Cy += self.dy
            drawHuman(canvas,self.Cx,self.Cy)
        self.right = self.Cx + self.R
        self.top = self.Cy - self.R
        self.bottom = self.Cy + self.R
        if self.dead == True:
            bloodSpray(canvas,self.Cx,self.Cy)

    def kill(self):
        self.dead = True 
        
class ShootEnemy(Actor):
    def __init__(self,canvasHeight,canvasWidth):
        self.canvasHeigh = canvasHeight
        self.canvasWidth = canvasWidth
        self.Cx = random.randint(300,canvasHeight-200)
        self.Cy = random.randint(300,canvasWidth -200)
        self.R = 20
        self.dead = False
        self.shootTime = 0
        self.left = self.Cx - self.R
        self.right = self.Cx + self.R
        self.top = self.Cy - self.R
        self.bottom = self.Cy + self.R
        self.shotsFired = []
        
    def draw(self,canvas,playerX,playerY,playerR):
        if self.dead != True:
            canvas.create_rectangle(self.Cx - self.R,self.Cy-self.R,
                                    self.Cx +self.R, self.Cy + self.R,
                                    fill = "black")
            #self.shootTime += 3
            #if self.shootTime % 15 == 0:
               # self.shotsFired.append(Wepon(self.Cx,self.Cy,self.R,playerX,
                #                                playerY))
        else:
            canvas.create_oval(self.Cx - self.R,self.Cy-self.R,
                                    self.Cx +self.R, self.Cy + self.R,
                                    fill = "red")  

                                    
    def enemyShots(self):
         return self.shotsFired
         
    def kill(self):
        self.dead = True
        
                                
        
    
class Tree(Actor):
    def __init__(self,canvasHeight,canvasWidth):
        self.canvasHeigh = canvasHeight
        self.canvasWidth = canvasWidth
        self.Cx = random.randint(50,canvasHeight-50)
        self.Cy = random.randint(50,canvasWidth -50)
        self.R = 20
        self.left = self.Cx - self.R
        self.right = self.Cx + self.R
        self.top = self.Cy - self.R
        self.bottom = self.Cy + self.R
        
    def draw(self,canvas,v1,v2,v3):
        Trunkx1 = self.Cx
        Trunkx2 = self.Cx
        Trunky1 = self.Cy 
        Trunky2 = self.Cy +50
        canvas.create_line(self.Cx,self.Cy,self.Cx,self.Cy+50,width = 10)
        canvas.create_line (self.Cx - 40,self.Cy + 30,self.Cx +40,self.Cy +30,
                                width = 10)
        canvas.create_line(self.Cx -30,self.Cy +20,self.Cx + 30, self.Cy + 20,
                                width = 10)
        canvas.create_line(self.Cx -20,self.Cy + 10,self.Cx + 20,self.Cy +10, 
                            width = 10)
        canvas.create_line(self.Cx -10,self.Cy,self.Cx +10,self.Cy,width = 10)
        
    def isTree(self):
        return True 
        
class Helth(Actor):
    def __init__(self,canvasHeight,canvasWidth):
        self.canvasHeight = canvasHeight
        self.canvasWidth = canvasWidth
        self.Cx = random.randint(100,canvasWidth-100)
        self.Cy = random.randint(100,canvasHeight -100)
        self.R = 20
        self.left = self.Cx - self.R
        self.right = self.Cx + self.R
        self.top = self.Cy - self.R
        self.bottom = self.Cy + self.R
        self.canDraw =True
        
           
        
    def draw(self,canvas,v1,v2,v3):
        canvas.create_rectangle(self.left,self.top,self.right,self.bottom,
                                fill = "black")
        canvas.create_rectangle(self.left - 5,self.top -5,self.right +5,
                                self.bottom +5, fill = "white")
        canvas.create_line(self.Cx,self.Cy - 10, self.Cx,self.Cy +10, 
                            fill = "red")
        canvas.create_line(self.Cx -10,self.Cy,self.Cx+10,self.Cy,
                            fill = "red")
        
    def isHealth(self):
        return True
        

        
class Fire(Actor):
    def __init__(self,canvasHeight,canvasWidth):
        self.canvasHeigh = canvasHeight
        self.canvasWidth = canvasWidth
        self.Cx = random.randint(50,canvasHeight-50)
        self.Cy = random.randint(50,canvasWidth -50)
        self.R = 20
        self.left = self.Cx - self.R
        self.right = self.Cx + self.R
        self.top = self.Cy - self.R
        self.bottom = self.Cy + self.R
        
class Pit(Actor):
    def __init__(self,canvasHeight,canvasWidth):
        self.canvasHeigh = canvasHeight
        self.canvasWidth = canvasWidth
        self.Cx = random.randint(50,canvasHeight-50)
        self.Cy = random.randint(50,canvasWidth -50)
        self.R = 100
        self.left = self.Cx - self.R
        self.right = self.Cx + self.R
        self.top = self.Cy - self.R
        self.bottom = self.Cy + self.R
        

    
class Invotory(object):
    def __init__(self,canvasWidth,canvasHeight):
        self.canvasWidth = canvasWidth
        self.canvasHeight = canvasHeight 
        
    def drawLife(self,canvas,hP):
        TextCx =  50 + 30 
        TextCy = 50 + 20
        canvas.create_text(TextCx,TextCy,text = "HP:",font =("imact",20))
        x1 = TextCx + 30
        y1 = TextCy
        x2 = x1 + (hP *5)
        if hP <=0:
            x2 = x1
        canvas.create_line(x1,y1,x2,y1,fill = "red",width = 5)
        

        


##############################################################################
# Start GAME CODE                                                           #
##############################################################################
# source: http://www.kosbie.net/cmu/spring-14/15-112/

def button1Pressed():
    # accesses canvas as a global variable
    Game(4,4).run()
    

def button2Pressed():
    Game(16,16).run()
    
    
def button3Pressed():
    Game(24,24).run()
    
def button4Pressed(canvas):
    canvas.data["help"] = True 
    redrawAll(canvas)
    
def button5Pressed(canvas):
    canvas.data["help"] = False
    redrawAll(canvas)
    
def redrawAll(canvas):
    canvas.delete(ALL)
    check = canvas.data["help"]
    if check  == True:
        canvas.create_rectangle(0,0,720,600,fill = "black")
        drawHelp(canvas)
        b5 = canvas.data["button5"]
        canvas.create_window(720/2, 500, window = b5)
        
    else: 
        canvas.create_rectangle(0,0,720,600,fill="BLACK")
        canvas.create_text(720/2, 200,text = "SPY MAZE",fill = "red",
                            font = ("Impact",50,"bold"))
        b1 = canvas.data["button1"]
        canvas.create_window(720/2-70, 400, window=b1)
        b2 = canvas.data["button2"]
        canvas.create_window(720/2 , 400, window=b2)
        b3 = canvas.data["button3"]
        canvas.create_window(720/2+70,400,window=b3)
        b4 = canvas.data["button4"]
        canvas.create_window(720/2, 400 +50, window = b4)

def drawHelp(canvas):
    canvas.create_rectangle(0,0, 720,600, fill = "black") 
    text1 = "You are a spy and lost in the enemy base,"
    text2 = "you must reach the end of the maze to complete the mission."
    text3 = "Use W, A, S, D to to contol player movment"
    text4 = "move the mosue to aim with the crosshairs, click to fire"
    text5 = "Avoid the following: "
    text6 = "press 'h' any time to show help in game"
    text7 ="Pick up health packs to replenish health "
    canvas.create_text( 720/2, 50, text = text1, fill = "red", font = ("impact",15,"bold"))
    canvas.create_text( 720/2, 80, text = text2, fill = "red", font = ("impact",15,"bold"))
    canvas.create_text(720/2, 110,text = text3, fill = "red", font = ("impact",15,"bold"))
    canvas.create_text(720/2, 140, text = text4 , fill = "red", font = ("impact",15,"bold"))
    canvas.create_text(720/2, 180, text = text5 , fill = "red", font = ("impact", 17,"bold"))
    canvas.create_text(720/2, 450, text = text6, fill = "red", font = ("impact",17,"bold"))
    canvas.create_text(720/2, 425, text = text7, fill = "red", font = ("impact",17,"bold"))
    canvas.create_rectangle(150, 300,  200, 400, fill = "white")
    drawHuman(canvas,175 ,350)
    canvas.create_text (720/2, 350 , text = "and", font = ("impact", 20,"bold"))
    bloodSpray(canvas,400, 350)
    
  
    
    
def init(root, canvas):

    b1 = Button(canvas, text="EASY", command=button1Pressed)
    canvas.data["button1"] = b1
    b2 = Button(canvas, text="NORMAL", command=button2Pressed)
    canvas.data["button2"] = b2
    b3 = Button(canvas,text = "HARD", command = button3Pressed)
    canvas.data["button3"] = b3
    b4 = Button(canvas,text =" LEARN TO PLAY", command= lambda: button4Pressed(canvas))
    canvas.data["button4"] = b4 
    b5 = Button (canvas,text = "RETURN", command = lambda: button5Pressed(canvas))
    canvas.data["button5"] = b5
    canvas.data["help"] =False 
    canvas.pack() 
    redrawAll(canvas)

def run():
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=720, height=562)
    # Store canvas in root and in canvas itself for callbacks
    root.canvas = canvas.canvas = canvas
    # Set up canvas data and call init
    canvas.data = { }
    init(root, canvas)

    root.mainloop()  
   
    
     
      
  # WAS NOT implented  
def playVideo():
    # source : http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html
    cap = cv2.VideoCapture('introvideo.mov')
    while(cap.isOpened()):
        ret,frame = cap.read()
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

run()


    
     

        



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        


