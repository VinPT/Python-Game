import random as rand
from collections import namedtuple


class LevelGenerator:
    level= []
    roomExitCalculator = Probability([30,55,15])
    
    def __init__(self, xSize, ySize): #zSize not included thus keeping it two dimentional for now.
        
        self.generateNewMap(xSize,ySize,1)
        roomNumber = Probability([30,55,15])
    
    def generateNewMap(self, xSize,ySize,Zsize):
        self.level = [[TempRoom for x in range(xSize)] for x in range(ySize)]
        
        print("Hello my size is " , len(self.level), len(self.level[0]))
        self.makeRoom("null","1f", 0, 0)

    def makeRoom(self, lastRoom, roomName , locx, locy):
        deepest = "null"
        depth = 0
        numberExits = self.roomExitCalculator.calculate()
        

        if self.level[locx][locy].roomName == "null":
            self.level[locx][locy].roomName = roomName
            
            #generate Exits
            #if 0 is returned for depth dont consider room generated



        else:
            deepest = roomName

        return depth, deepest    
        




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
                result = x
                break

        return result

        
        
class TempRoom:
    roomName = "null";
    connectedRooms = [];

    
    
p1 = LevelGenerator(10,10)
p1.generateNewMap(1,1,1)


1 # 60%
2 # 10%
3 #  5%
4 # 15%