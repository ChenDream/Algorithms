import sys

class Heap():
    def __init__(self,lst):
        self.lst = lst
        self.heapSize = len(self.lst)
        self.lst.insert(0,sys.maxsize)
        # self.BuildHeap()
    def BuildHeap(self):

        lens = int((len(self.lst)-1)/2)+1
        # lens = int(len(self.lst) / 2)
        for i in range(1,lens):
            self.Heap(lens-i)
    def Heap(self,i):
        return
    def Parent(self,i):
        return int(i/2)
    def Left(self,i):
        return 2*i
    def Right(self,i):
        return 2*i+1
    def exchange(self,i):
        temp = self.lst[1]
        self.lst[1] = self.lst[i]
        self.lst[i] = temp
    def HeapDelete(self,i):
        if i>self.heapSize:
            return "index out of range"
        if i == self.heapSize:
            self.heapSize -= 1
            return
        print("key is: ",self.lst[i])
        self.lst[i] = self.lst[self.heapSize]
        self.heapSize -= 1
        self.Heap(i)
    def miusHeapSize(self):
        self.heapSize -= 1
    def getList(self):
        return self.lst
    def printLst(self):
        print(self.lst[1:self.heapSize+1])
    def __str__(self):
        return str(self.lst[1:])
class MinHeap(Heap):
    def Heap(self,i):
        left =self.Left(i)
        right = self.Right(i)

        if left < self.heapSize and self.lst[left]<self.lst[i]:
            smallest = left
        else:
            smallest = i
        if right< self.heapSize and self.lst[right]<self.lst[smallest]:
            smallest = right
        if smallest!=i:
            temp = self.lst[i]
            self.lst[i] = self.lst[smallest]
            self.lst[smallest] = temp
            self.Heap(smallest)

    # following functions are for priority queues
    def HeapMinimum(self):
        return self.lst[1]
    def HeapExtractMin(self):
        if self.heapSize <1:
            return "heap underflow"
        min = self.lst[1]
        self.lst[1] = self.lst[self.heapSize]
        self.heapSize -=1
        self.Heap(1)
        return min
    def HeapIncreaseKey(self,i,key):
        if key >self.lst[i]:
            return "new key is larger than current key"
        self.lst[i] = key
        while i>1 and self.lst[self.Parent(i)]>self.lst[i]:
            parentIndex = self.Parent(i)
            temp = self.lst[i]
            self.lst[i] = self.lst[parentIndex]
            self.lst[parentIndex] = temp
            i =  parentIndex
    def MinHeapInsert(self,key):
        self.heapSize +=1
        self.lst.append(-sys.maxsize)
        self.HeapIncreaseKey(self.heapSize,key)
class MaxHeap(Heap):
    def Heap(self,i):

        left =self.Left(i)
        right = self.Right(i)
        if left <= self.heapSize and self.lst[left]>self.lst[i]:
            largest = left
        else:
            largest = i
        if right<= self.heapSize and self.lst[right]>self.lst[largest]:
            largest = right
        if largest!=i:
            temp = self.lst[i]
            self.lst[i] = self.lst[largest]
            self.lst[largest] = temp
            self.Heap(largest)

    # following functions are for priority queues
    def HeapMaximum(self):
        return self.lst[1]
    def HeapExtractMax(self):
        if self.heapSize<1:
            return "heap underflow"
        max = self.lst[1]
        self.lst[1] = self.lst[self.heapSize]
        self.heapSize -=1
        self.Heap(1)
        return max
    def HeapIncreaseKey(self,i,key):
        if key < self.lst[i]:
            return "new key is smaller than current key"
        self.lst[i] = key
        while i>1 and self.lst[self.Parent(i)]<self.lst[i]:
            partentIndex = self.Parent(i)
            temp = self.lst[i]
            self.lst[i] = self.lst[partentIndex]
            self.lst[partentIndex] = temp
            i = partentIndex
    def MaxHeapInsert(self,key):
        self.heapSize +=1
        # self.lst[self.heapSize] = -sys.maxsize
        self.lst.append(-sys.maxsize)
        self.HeapIncreaseKey(self.heapSize,key)