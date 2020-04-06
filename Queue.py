class Queue:
    queue = []


    def inqueue(self, data):
        self.queue.append(data)
    # returns a value based on the probabilitys provided during init              
    def dequeue(self):
        return self.queue.pop(0) 
    
    def size(self):
        return len(self.queue)