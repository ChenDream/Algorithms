
# stack implements a last-in,first-out or LIFO

class Stack():
    def __init__(self):
        # the index of list start at 0 not 1
        self.top = -1
        self.lst = []
    def empty(self):
        if self.top == -1:
            return True
        return False
    def push(self,x):
        self.top +=1
        try:
            self.lst[self.top] = x
        except IndexError:
            self.lst.append(x)

    def pop(self):
        if self.empty():
            return "underflow"
        else:
            self.top -= 1
            return self.lst[self.top+1]

if __name__ == "__main__":
    stack = Stack()
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
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())


