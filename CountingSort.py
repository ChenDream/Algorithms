
# counting sort is stable sort which means if a1 == a2 and index of a1 < index of a2
# after counting sort index of a1 is still less than index of a2
class CountingSort():
    def __init__(self,lst,k):
        # self.b is result sorted list, self.c is temp list with k size, self.k is largetest elements on the list
        self.lst = lst
        self.b = []
        self.c = []
        self.k = k
    def sort(self):
        for i in range(0,self.k+1):
            self.c.append(0)

        lstLen = len(self.lst)
        for i in range(lstLen+1):
            self.b.append(0)
        for j in range(0,lstLen):
            self.c[self.lst[j]] = self.c[self.lst[j]]+1
        # self.c[i] contains the number of elements equal to i

        for k in range(1,self.k+1):
            self.c[k] = self.c[k]+self.c[k-1]

        # self.c[i] contains the number of elements less than or equal to i

        for l in range(lstLen):
            # m = lstLen -  l-1
            m = l
            self.b[self.c[self.lst[m]]] = self.lst[m]
            self.c[self.lst[m]] = self.c[self.lst[m]] - 1

        return self.b[1:]




if __name__ == "__main__":
    a = [16, 14, 10, 8, 7, 9, 3, 2, 4, 5]
    b = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]
    # c = [6,0,2,0,1,3,4,6,1,3,2]
    cs = CountingSort(b,15)
    z = cs.sort()
    print(z)