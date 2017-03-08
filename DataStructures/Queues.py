# queues implements a first-in,first-out or FIFO
# the queue has a head and a tail

#queues with fixed size
MAX_SIZE = 10
class Queues():
    def __init__(self):

        self.lst = [0]*MAX_SIZE
        self.head = 0
        self.tail = 0

    def enqueue(self,x):
        tail_temp = 0
        if self.tail == MAX_SIZE-1:
            tail_temp = 0
        else:
            tail_temp = self.tail +1

        if self.head == tail_temp:
            return "queues overflows"

        self.lst[self.tail] = x

        self.tail = tail_temp

    def dequeue(self):
        if self.head == self.tail:
            return "queues overflows"
        x = self.lst[self.head]
        if self.head == MAX_SIZE-1:
            self.head = 0
        else:
            self.head +=1
        return x

if __name__ == "__main__":
    queues = Queues()

    print(queues.enqueue(1))
    print(queues.enqueue(2))
    print(queues.enqueue(3))
    print(queues.enqueue(4))
    print(queues.enqueue(5))
    print(queues.enqueue(6))
    print(queues.enqueue(7))
    print(queues.enqueue(8))
    print(queues.enqueue(9))
    print(queues.enqueue(10))
    print(queues.enqueue(11))
    print(queues.dequeue())
    print(queues.dequeue())
    print(queues.dequeue())
    print(queues.dequeue())
    print(queues.dequeue())
    print(queues.dequeue())
    print(queues.dequeue())
    print(queues.dequeue())
    print(queues.dequeue())
    print(queues.dequeue())
    print(queues.dequeue())
    print(queues.dequeue())
    print(queues.dequeue())


