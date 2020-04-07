import random as rand
from Room import TempRoom
from Probability import Probability
from Queue import Queue



class LevelGenerator:
    level= []
    generationQueue = Queue()
    
    def __init__(self, xSize, ySize): #zSize not included thus keeping it two dimentional for now.
        
        self.generateNewMap(xSize,ySize,1)
            
    
    def generateNewMap(self, xSize,ySize,Zsize):
        self.level = [[TempRoom("none",-1,-2,-2) for x in range(xSize)] for y in range(ySize)]
        
        print("Hello my size is " , len(self.level), len(self.level[0]))       #i think it is Y X this might get me later 

        #make fake room to make this work inelegent but it works
        
        #set up while loop;
        choices = ["L","F","R"]
        #deepestNode = 0 #place holder for when finding boss room later
        roomExitCalculator = Probability([33,33,34])
        self.generationQueue.inqueue(NodeSave(5, 4,"0F", 5, 5, 0))
        
        while(self.generationQueue.size() > 0):
            nodeData = self.generationQueue.dequeue()
            locX = nodeData.locX
            locY = nodeData.locY
            depth = nodeData.depth


            selectDirection = rand.randint(0,2)
            numberExits = roomExitCalculator.calculate()
            
            #check slot is not occupyed
            # old test statement print("this rooms name is "+self.level[locx][locy].roomName, locx, locy)
            if self.level[locX][locY].roomName == "none":
                
                #set room values
                self.level[locX][locY].roomName = nodeData.roomName
    #print("room name", nodeData.roomName)
                self.level[locX][locY].xloc = locX
                self.level[locX][locY].yloc = locY
                self.level[locX][locY].depth = depth
                
                #generate Exits
                #if 0 is returned for depth dont consider room generated
    #print("number exits", numberExits)

                
                #Generate children rooms
                for x in range(numberExits):
                    #Generate children needs a better algorithm that makes sure of problems
                    #pick direction of next room 
                    newLocX = locX
                    newLocY = locY
                    xdif = locX - nodeData.lastRoomX
                    ydif = locY - nodeData.lastRoomY
                    roomLetter = choices[ (selectDirection + x) % 3]

                    if (roomLetter == "F"):
                        newLocX = newLocX + xdif
                        newLocY = newLocY + ydif
                        name = "{}F".format(depth+1)

                    elif (roomLetter == "L"):
                        newLocX = newLocX - ydif
                        newLocY = newLocY + xdif
                        name = "{}L".format(depth+1)
                
                    elif (roomLetter == "R"):
                        newLocX = newLocX + ydif
                        newLocY = newLocY - xdif
                        name = "{}R".format(depth+1)
                    

                    if (newLocX < 0 or newLocY < 0 or newLocX >= len(self.level)  or newLocY >= len(self.level[0])):
                            print("Temp was none on node" , newLocX, newLocY)
                    else:
                        self.generationQueue.inqueue(NodeSave(locX, locY, name, newLocX, newLocY, depth+1))

    
    def printLevel(self):
        for i in range(len(self.level[0])):
            for j in range(len(self.level)):
                for k in range(6-len(self.level[i][j].roomName)):
                    print(end=' ')
                print(self.level[i][j].roomName,end='')
               #S print(len(self.level[i][j].roomName))
            print(end='\n')
        return None
    


#a struct of data to save for use with GeneratorQueue
class NodeSave:
    lastRoomX = 0
    lastRoomY = 0
    roomName = "none"
    locX = 0
    locY = 0
    depth = 0

    def __init__(self, inputLastRoomX, inputLastRoomY, roomName, inputLocX, inputLocY, inputDepth):
        self.lastRoomX = inputLastRoomX
        self.lastRoomY = inputLastRoomY
        self.roomName = roomName
        self.locX = inputLocX
        self.locY = inputLocY
        self.depth = inputDepth
        
        

        
    
p1 = LevelGenerator(35,35)
p1.printLevel()
#p1.generateNewMap(1,1,1)


1 # 60%
2 # 10%
3 #  5%
4 # 15%