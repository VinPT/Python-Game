import random as rand
from collections import namedtuple


class LevelGenerator:
    level= []

    
    def __init__(self, xSize, ySize): #zSize not included thus keeping it two dimentional for now.
        
        self.generateNewMap(xSize,ySize,1)
            
    
    def generateNewMap(self, xSize,ySize,Zsize):
        self.level = [[TempRoom for x in range(xSize)] for x in range(ySize)]
        
        print("Hello my size is " , len(self.level), len(self.level[0]))       #i think it is Y X this might get me later 
        self.makeRoom(None,"1f", 0, 0)

    def makeRoom(self, lastRoom, roomName , locx, locy):
        deepestNode = None
        depth = 0
        choices = ["L","F","R"]
        roomExitCalculator = Probability([30,55,15])
        numberExits = roomExitCalculator.calculate()
        

        if self.level[locx][locy].roomName == "none":
            self.level[locx][locy].roomName = roomName
            
            #generate Exits
            #if 0 is returned for depth dont consider room generated
            print("number exits", numberExits)

            for x in range(numberExits):
                self.makeRoom(self.level[locx][locy], "2F", 1, 1)

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
            return name, thisRoom.locx, thisRoom.locy
        




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

    
    
p1 = LevelGenerator(10,10)
#p1.generateNewMap(1,1,1)


1 # 60%
2 # 10%
3 #  5%
4 # 15%