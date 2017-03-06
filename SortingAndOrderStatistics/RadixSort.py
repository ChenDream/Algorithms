import math
class RadixSort():
    def __init__(self,lst,d):
        self.lst = lst
        self.d = d
        self.bucket = []
        self.cleanBucket()
    def sort(self):
        for i in range(1,self.d+1):
            self.cleanBucket()
            for j in range(len(self.lst)):
                temp =(self.lst[j]/10**(i-1))%10

                self.bucket[int(temp)].append(self.lst[j])
            self.lst = []
            for k in range(len(self.bucket)):
                if len(self.bucket[k])==0:
                    continue
                if len(self.bucket[k])==1:
                    self.lst.append(self.bucket[k][0])
                    continue
                for l in range(len(self.bucket[k])):
                    self.lst.append(self.bucket[k][l])
        return self.lst
    def cleanBucket(self):
        self.bucket = []
        for i in range(0,10):
            self.bucket.append([])

if __name__ == "__main__":
    a = [329,457,657,839,436,720,355]

    rs = RadixSort(a,3)
    a = rs.sort()
    print(a)