
class DoubleLinkedList:
    def __init__(self,key):
        self.head = None

    def search(self,key):
        x = self
        while x != None and x.key != key:
            x = x.next
        return x

    def insert(self,x):
        x.next = self


class LinkNode:
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None

    def getkey(self):
        return self.key

if __name__ == "__main__":

    doublelist = DoubleLinkedList

