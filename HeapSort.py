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
def HeapSort(lst):
    maxheap = MaxHeap(lst)
    maxheap.BuildHeap()
    lens = len(maxheap.getList())
    for i in range(2,lens):
        l = lens - i+1
        maxheap.exchange(l)
        maxheap.miusHeapSize()
        maxheap.Heap(1)
    lst.pop(0)

if __name__ == "__main__":
    c = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    a = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    d = [5,13,2,25,7,17,20,8,4]
    f = [4, 1, 3, 2, 16, 9]
    b = [15,13,9,5,12,8,7,4,0,6,2,1]

    # HeapSort(f)
    # print(f)

    maxheap = MaxHeap(b)
    maxheap.BuildHeap()
    print(maxheap)
    # while maxheap.heapSize>0:
    #     print(maxheap.HeapExtractMax())
    #     maxheap.printLst()
    maxheap.MaxHeapInsert(10)
    maxheap.printLst()