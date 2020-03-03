import random as rand
from collections import namedtuple


class LevelGenerator:
    level= []

    
    def __init__(self, xSize, ySize): #zSize not included thus keeping it two dimentional for now.
        
        self.generateNewMap(xSize,ySize,1)
            
    
    def generateNewMap(self, xSize,ySize,Zsize):
        self.level = [[TempRoom("none",-1,-2,-2) for x in range(xSize)] for x in range(ySize)]
        
        print("Hello my size is " , len(self.level), len(self.level[0]))       #i think it is Y X this might get me later 

        #make fake room to make this work inelegent but it works
        fakeRoom = TempRoom("Fakeroom",-1,-1,0)

        self.makeRoom(fakeRoom,"1f", 2, 2)

    def makeRoom(self, lastRoom, roomName , locx, locy):
        deepestNode = None
        depth = 0

        choices = ["L","F","R"]
        selectDirection = rand.randint(0,2)

        roomExitCalculator = Probability([30,55,15])
        numberExits = roomExitCalculator.calculate()
        
        #check slot is not occupyed
        print("this rooms name is "+self.level[locx][locy].roomName, locx, locy)
        if self.level[locx][locy].roomName == "none":
            
            #set room values
            self.level[locx][locy].roomName = roomName
            self.level[locx][locy].xloc = locx
            self.level[locx][locy].yloc = locy
            
            #generate Exits
            #if 0 is returned for depth dont consider room generated
            print("number exits", numberExits)

            
            #Generate children rooms
            #Generate children needs a better algorithm that makes sure of problems
            for x in range(numberExits):
                temp = self._nextRoomDataGenerator(lastRoom, self.level[locx][locy], choices[ (selectDirection + x) % 3])
                if temp is not None:
                    self.makeRoom(self.level[locx][locy], temp[0], temp[1], temp[2])
                else:
                    print("Temp was none on node" , locx, locy)

        else:
            deepestNode = roomName

        return depth, deepestNode    

    def _nextRoomDataGenerator(self, lastRoom,thisRoom,roomLetter):
        name = "neyt"
        locx = 0
        locy = 0
        xdif = thisRoom.xloc - lastRoom.xloc
        ydif = thisRoom.yloc - lastRoom.yloc

        if (roomLetter == "F"):
            locx = thisRoom.xloc + xdif
            locy = thisRoom.yloc + ydif

        elif (roomLetter == "L"):
            locx = thisRoom.xloc + ydif
            locy = thisRoom.yloc + xdif
    
        elif (roomLetter == "R"):
            locx = thisRoom.xloc - ydif
            locy = thisRoom.yloc - xdif
        

        if (locx < 0 or locx < 0 or locx >= len(self.level)  or locy >= len(self.level[0])):
            return None
        else:
            return name, locx, locy
        




class Probability:
    probabilityArr = []
    totalProbablility = 0
    def __init__(self, probabilityArray): #zSize not included thus keeping it two dimentional for now.
        
        self.probabilityArr = probabilityArray.copy()
        
        for x in range (len(self.probabilityArr)):
            self.totalProbablility = self.totalProbablility + self.probabilityArr[x]


    # returns a value based on the probabilitys provided during init              
    def calculate(self):
        result = 1
        threshhold = 0
        random = rand.randint(1,self.totalProbablility)

        
        for x in range (len(self.probabilityArr)):
            threshhold = threshhold + self.probabilityArr[x]

            if threshhold > random:
                result = x + 1
                break

        return result

        
        
class TempRoom:
    roomName = "none";
    depth = 0
    xloc = 0
    yloc = 0
    connectedRooms = [];

    def __init__(self, roomName, depth, xloc, yloc):
        self.roomName = roomName
        self.depth = depth
        self.xloc = xloc
        self.yloc = yloc
        
    
p1 = LevelGenerator(10,10)
#p1.generateNewMap(1,1,1)


1 # 60%
2 # 10%
3 #  5%
4 # 15%