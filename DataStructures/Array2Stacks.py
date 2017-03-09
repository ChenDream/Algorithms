
# implement two stacks in one array A[0....N] in such that neither stack overflows unless the total
# number of elements in both stacks together is n
MAXSIZE = 10
class myArrays():
    def __init__(self):
        self.lst = [0]*MAXSIZE
        self.top1 = -1
        self.top2 = MAXSIZE
        self.switch = 1


    def empty(self,flag=0):
        if self.top1 == -1 and self.top2 ==MAXSIZE:
            return True
        if flag == 1 and self.top1 == -1:
            return True
        if flag == 2 and self.top2 == MAXSIZE:
            return True
        return False

    def push(self,x,flag=1):
        if flag == 1:
            self.top1 += 1
            if self.top1 >= self.top2:
                print("Stack 1 push Overflow",x)
                self.top1 -=1
                return
            self.lst[self.top1] = x
        elif flag == 2:
            self.top2 -= 1
            if self.top2 <= self.top1:
                print("Stack 2 push Overflow",x)
                self.top2 +=1
                return
            self.lst[self.top2] = x
        print("Stack",flag,"push",x)

    def pop(self,flag = 1):
        result = 0
        if self.empty(flag):
            print("Stack",flag,"pop Underflow")
            return
        if flag == 1:
            self.top1 -= 1
            result = self.lst[self.top1 + 1]
        if flag == 2:
            self.top2 +=1
            result = self.lst[self.top2 -1]
        print("Stack",flag,"pop",result)
        return result

if __name__ == "__main__":

    myArray = myArrays()

    myArray.push(1)
    myArray.push(2)
    myArray.push(3)
    myArray.push(4)
    myArray.push(5)
    myArray.push(6)
    myArray.push(7)
    myArray.push(8)
    myArray.push(9)
    myArray.push(10)
    myArray.push(11)

    myArray.push(20,2)
    myArray.push(19,2)

    myArray.pop()
    myArray.push(18,2)
    myArray.push(17, 2)
    myArray.pop(2)



