
# stack implements a last-in,first-out or LIFO

MAXSIZE = 10
class Stack():
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
            print(self.lst[self.top+1])
            return self.lst[self.top+1]


if __name__ == "__main__":
    stack = Stack(10)
    stack.push(3)
    stack.push(4)
    print(stack.pop())
    stack.push(5)
    print(stack.pop())
    stack.push(6)
    stack.push(7)
    stack.push(8)
    stack.push(9)
    stack.push(10)
    stack.push(11)
    stack.push(12)
    stack.push(13)
    stack.push(14)
    stack.push(15)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())


