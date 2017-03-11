import random
from SortingAndOrderStatistics.Heap import MaxHeap,MinHeap
from DataStructures.Queues import Queue
#implement first-in first-out with priority queue
#implement stack with priority queue

#TODO: minheap has bug that pop will return int.MIN number
class PriorityQueues():
    def __init__(self,type=max):
        if type == max:
            self.type = True
        else:
            self.type = False
        if self.type:
            self.maxheap = MaxHeap([])
        else:
            self.minheap = MinHeap([])
    def pop(self):
        if self.type:
            return self.maxheap.HeapExtractMax()
        else:
            return self.minheap.HeapExtractMin()
    def push(self,x):
        if self.type:
            self.maxheap.MaxHeapInsert(x)
        else:
            self.minheap.MinHeapInsert(x)
    def top(self):
        if self.type:
            return self.maxheap.HeapMaximum()
        else:
            return self.minheap.HeapMinimum()
if __name__ == "__main__":
    pq = PriorityQueues()
    lst = []
    for i in range(15):
        i = random.randint(1,100)
        lst.append(i)
        pq.push(i)

    for i in range(15):
        print(pq.pop())
    print(lst)

