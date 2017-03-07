# queues implements a first-in,first-out or FIFO
# the queue has a head and a tail

MAX_SIZE = 100
class Queues():
    def __init__(self):

        self.lst = [MAX_SIZE]
        self.head = 0
        self.tail = 0

    def enqueue(self,x):
        self.lst[self.tail] = x
        if self.tail == MAX_SIZE:
            self.tail = 0
        else:
            self.tail +=1
    def dequeue(self):
        x = self.lst[self.head]
        if self.head == MAX_SIZE:
            self.head = 0
        else:
            self.head +=1
        return x

if __name__ == "__main__":
    queues = Queues()
