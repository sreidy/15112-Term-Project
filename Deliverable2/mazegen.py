# source: http://www.migapro.com/depth-first-search/
import random
import math

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
        exitCol = 2
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
    

print2dList(makeMaze(50,15))
