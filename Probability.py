import random as rand

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