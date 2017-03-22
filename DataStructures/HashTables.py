
MAXNUM = 100
class TableNode:
    def __init__(self,k,v):
        self.key,self.value = k,v

class DirectAddressTable:
    def __init__(self):
        self.lst = [0]*MAXNUM

    def search(self,k):
        return self.lst[k]

    def insert(self,x):

        self.lst[x.key] = x

    def delete(self,x):
        self.lst[x.key] = None

class BitVector:
    def __init__(self):
        self.lst = [False]*MAXNUM

    def search(self,k):
        return self.lst[k]

    def insert(self,k):
        self.lst[k] = True

    def delete(self,k):
        self.lst[k] = False

if __name__ == "__main__":
    # table = DirectAddressTable()
    # for i in range(13):
    #     table.insert(TableNode(i,i+1))
    #
    # for i in range(13):
    #     print(table.search(i).value)
    #
    # for i in range(13):
    #     table.delete(TableNode(i,0))

    bv = BitVector()
    bv.insert(4)
    print(bv.search(4))