from DataStructures.LinkedList import SingleLinkList,LinkNode


# stack implements a last-in,first-out or LIFO
class Stack:
    def __init__(self,size):
        # the index of list start at 0 not 1
        self.size = size
        self.top = -1
        self.lst = [0]*self.size

    def empty(self):
        if self.top == -1:
            return True
        return False

    def push(self,x):
        # list without maxsize
        # try:
        #     self.lst[self.top] = x
        # except IndexError:
        #     self.lst.append(x)
        if self.top+1 >= self.size:
            print("push",x,"overflow")
            return
        else:
            self.top += 1
            self.lst[self.top] = x

    def pop(self):
        if self.empty():
            print("pop","underflow")
            return
        else:
            self.top -= 1
            # print(self.lst[self.top+1])
            return self.lst[self.top+1]

# this queue class is used by implementing stack with 2 queue
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
        return False

    def getCount(self):
        return self.count

# implement stack with 2 queues
class Stack_q():
    def __init__(self,size):
        self.size = size
        self.queue1 = Queue(self.size)
        self.queue2 = Queue(self.size)
        self.size = 0

    def push(self,x):
        if self.queue1.isEmpty() and self.queue2.isEmpty():
            self.queue1.enqueue(x)
            return
        if not self.queue1.isEmpty():
            self.queue1.enqueue(x)
            return
        if not self.queue2.isEmpty():
            self.queue2.enqueue(x)
            return

    def pop(self):
        if self.queue1.isEmpty() and self.queue2.isEmpty():
            print("stack underflow")
            return
        if not self.queue1.isEmpty():

            count = self.queue1.getCount()
            for i in range(count-1):
                self.queue2.enqueue(self.queue1.dequeue())
            return self.queue1.dequeue()
        if not self.queue2.isEmpty():

            count = self.queue2.getCount()
            for i in range(count -1):
                self.queue1.enqueue(self.queue2.dequeue())
            return self.queue2.dequeue()


# implement a stack using a singly linked list
class Stack_LinkList:
    def __init__(self,size):
        self.size = size
        self.count = 0
        self.linklist = SingleLinkList()

    def empty(self):
        return self.linklist.empty()

    def push(self,x):
        if self.count == self.size:
            print("stack overflow")
            return
        self.count +=1
        node = LinkNode(x)
        self.linklist.insert(node)

    def pop(self):
        if self.count == 0:
            print("stack underflow")
            return
        x = self.linklist.head
        self.linklist.delete(self.linklist.head)
        self.count -=1
        return x.key

if __name__ == "__main__":
    stack_l = Stack_LinkList(10)
    for i in range(12):
        stack_l.push(i)
    for i in range(12):
        print(stack_l.pop())


    # stack_q = Stack_q(10)
    # for i in range(11):
    #     stack_q.push(i)
    #
    # for i in range(11):
    #     print(stack_q.pop())

    # stack = Stack(10)
    # stack.push(3)
    # stack.push(4)
    # print(stack.pop())
    # stack.push(5)
    # print(stack.pop())
    # stack.push(6)
    # stack.push(7)
    # stack.push(8)
    # stack.push(9)
    # stack.push(10)
    # stack.push(11)
    # stack.push(12)
    # stack.push(13)
    # stack.push(14)
    # stack.push(15)
    # print(stack.pop())
    # print(stack.pop())
    # print(stack.pop())
    # print(stack.pop())
    # print(stack.pop())
    # print(stack.pop())
    # print(stack.pop())
    # print(stack.pop())


