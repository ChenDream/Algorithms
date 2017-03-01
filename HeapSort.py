import sys
from Heap import MaxHeap,MinHeap

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

    maxheap = MaxHeap(c)
    maxheap.BuildHeap()

    print(maxheap)

    # while maxheap.heapSize>0:
    #     print(maxheap.HeapExtractMax())
    #     maxheap.printLst()
    maxheap.MaxHeapInsert(10)
    maxheap.printLst()
    maxheap.HeapDelete(3)
    maxheap.printLst()