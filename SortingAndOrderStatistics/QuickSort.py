import random,time

# def time_cost(fn):
#     def _wrapper(*args, **kwargs):
#         start = time.clock()
#         fn(*args, **kwargs)
#         print( "%s cost %s second"%(fn.__name__, time.clock() - start))
#     return _wrapper

class QuickSort():
    def __init__(self,lst,increase=True):
        self.lst = lst
        self.increase = increase


    def quicksort(self,p,r):
        if p<r:
            if self.increase:
                q = self.partition(p,r)
            else:
                q = self.partition_d(p,r)
            self.quicksort(p,q-1)
            self.quicksort(q+1,r)
    # increase order
    def partition(self,p,r):
        self.same = True
        x = self.lst[r]
        i =  p -1
        for j in range(p,r):
            if x != self.lst[j]:
                self.same = False
            if self.lst[j]<=x:
                i+=1
                temp = self.lst[i]
                self.lst[i] = self.lst[j]
                self.lst[j] = temp
        temp = self.lst[i+1]
        self.lst[i+1] = self.lst[r]
        self.lst[r] = temp
        if self.same:
            return int((p+r)/2)
        return i + 1
    # decrease order
    def partition_d(self,p,r):
        self.same = True
        x = self.lst[r]
        i = p-1
        for j in range(p,r):
            if x != self.lst[j]:
                self.same = False
            if self.lst[j]>=x:
                i+=1
                temp = self.lst[i]
                self.lst[i] = self.lst[j]
                self.lst[j] = temp
        temp = self.lst[i+1]
        self.lst[i+1] = self.lst[r]
        self.lst[r] = temp
        if self.same:
            return int((p+r)/2)
        return i+1


class RandomizedQuickSort(QuickSort):
    def __init__(self,lst,increase=True):
        super(RandomizedQuickSort, self).__init__(lst,increase)


    def randomizedPartition(self,p,r):
        i = random.randint(p,r)
        temp = self.lst[r]
        self.lst[r] = self.lst[i]
        self.lst[i] = temp
        if self.increase:
            return self.partition(p,r)
        else:
            return self.partition_d(p,r)


    def randomizedQuickSort(self,p,r):
        if p<r:
            q = self.randomizedPartition(p,r)

            self.randomizedQuickSort(p,q-1)
            self.randomizedQuickSort(q+1,r)


if __name__ == "__main__":
    # a = [5, 2, 4, 7, 1, 3, 2, 6, 5, -1]
    a = [16, 14, 10, 8, 7, 9, 3, 2, 4, 5]
    b = [16, 14, 10, 8, 7, 9, 3, 2, 4, 5]
    # a = [2,3,8,8,8,8,8,1]
    # a = [2,1,3,4]
    start = time.clock()
    qs = QuickSort(a)
    qs.quicksort(0,len(a)-1)
    print(a,time.clock()-start)

    start1 = time.clock()
    rqs = RandomizedQuickSort(b)
    rqs.randomizedQuickSort(0,len(b)-1)
    print(b,time.clock()-start1)
