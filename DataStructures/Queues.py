from DataStructures.Stacks import Stack
# queues implements a first-in,first-out or FIFO
# the queue has a head and a tail

#queues with fixed size
MAX_SIZE = 10
class Queue():
    def __init__(self,size):
        self.size = size
        self.lst = [0]*self.size
        self.head = 0
        self.tail = 0
        # count available elements on the list
        # also used for check overflows and underflows
        self.count = 0
    def enqueue(self,x):
        if self.count == self.size:
            print("enqueue",x,"overflows")
            return

        self.lst[self.tail] = x
        self.count +=1
        if self.tail == self.size - 1:
            self.tail = 0
        else:
            self.tail = self.tail + 1


    def dequeue(self):
        if self.count == 0:
            print("dequeue underflows")
            return
        x = self.lst[self.head]
        self.count -= 1
        if self.head == self.size-1:
            self.head = 0
        else:
            self.head +=1
        return x
    def isEmpty(self):
        if self.head == self.tail and self.count == 0:
            return True
        return  False
# Deque is  double end queue allows insertion and deletion at
# both end
class Deque():
    def __init__(self,size):
        self.size = size
        self.lst = [0]*self.size
        self.head = 0
        self.tail = 0
        self.count = 0

    def enqueue_front(self,x):
        if self.count == self.size:
            print("enqueue",x,"overflows")
            return

        self.lst[self.tail] = x
        self.count +=1

        if self.tail == self.size - 1:
            self.tail = 0
        else:
            self.tail += 1

    def enqueue_end(self,x):
        temp = 0
        if self.head == 0:
            temp = self.size -1
        else:
            temp = self.head -1
        if self.count == self.size:
            print("enqueue_end",x,"overflows")
            return
        self.lst[temp] = x
        self.count += 1
        self.head =temp

    def dequeue_front(self):
        temp = 0
        if self.tail ==0:
            temp = self.size - 1
        else:
            temp = self.tail - 1

        if self.count == 0:
            print("dequeue_front underflows")
            return
        x = self.lst[temp]
        self.count -=1
        self.tail = temp
        return x
    def dequeue_end(self):
        if self.count == 0:
            print("dequeue underflows")
            return
        x = self.lst[self.head]
        self.count -= 1
        if self.head == self.size-1:
            self.head = 0
        else:
            self.head +=1
        return x

# implement queues with two stacks
# enqueue push x in to stack_enqueue
# dequeue: if  stack_dequeue is empty,pop everything from stack_enqueue to stack_dequeue
# then pop stack_dequeue, if stack_dequeue is not empty, pop stack_dequeue
# advantage of using queues with two stack, the size of queue is flexible, from n to 2n
class Queue_s():
    def __init__(self,size):
        self.size =size
        self.stack_enqueue = Stack(self.size)
        self.stack_dequeue = Stack(self.size)

    def enqueue(self,x):
        self.stack_enqueue.push(x)

    def dequeue(self):
        if self.stack_dequeue.empty():
            while self.stack_enqueue.empty() is not False:
            # for i in range(self.size):
                self.stack_dequeue.push(self.stack_enqueue.pop())

        self.stack_dequeue.pop()
if __name__ == "__main__":

    # queues = Queue(10)
    # for i in range(11):
    #     queues.enqueue(i)
    # for i in range(11):
    #     print(queues.dequeue())
    # print(queues.isEmpty())

    # deque = Deque(10)
    # for i in range(11):
    #     deque.enqueue_front(i)
    #
    # for i in range(6):
    #     print(deque.dequeue_front())
    #     print(deque.dequeue_end())

    queue_s = Queue_s(10)
    for i in range(11):
        queue_s.enqueue(i)

    queue_s.dequeue()
    # for i in range(11):
    #     queue_s.dequeue()

