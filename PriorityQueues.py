
from Heap import MinHeap,MaxHeap

# class PriorityQueues():

if __name__ == "__main__":
    b = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    maxheap = MaxHeap(b)
    maxheap.BuildHeap()
    print(maxheap)