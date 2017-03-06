import math
from QuickSort import QuickSort
from InsertionSort import insertionSort
class BucketSort():
    def __init__(self,lst,BUCKET_SIZE = 10):
        self.lst = lst
        self.bucket =[]
        self.min = lst[0]
        self.max = lst[0]
        self.result = []
        for i in range(len(lst)):
            if lst[i]< self.min:
                self.min = lst[i]
            elif lst[i] > self.max:
                self.max = lst[i]
        self.bucketSize = BUCKET_SIZE
        self.bucketCount = math.floor((self.max - self.min)/self.bucketSize)+1
    def sort(self):
        n = len(self.lst)
        for i in range(self.bucketCount):
            self.bucket.append([])
        for i in range(n):
            self.bucket[math.floor((self.lst[i]-self.min)/self.bucketSize)].append(self.lst[i])
        m = len(self.bucket)

        for i in range(m):
            k = len(self.bucket[i])
            if k==1:
                self.result.append(self.bucket[i][0])
            if k==0:
                continue
            qs = QuickSort(self.bucket[i])
            qs.quicksort(0,len(self.bucket[i])-1)
            for j in range(k):
                self.result.append(self.bucket[i][j])
        return self.result
if __name__ == "__main__":
    b = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1,34,29,100,492,43,21,3,493,99]
    bs = BucketSort(b)
    print(bs.sort())
