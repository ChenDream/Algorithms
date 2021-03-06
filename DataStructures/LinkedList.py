

class LinkNode:
    def __init__(self,key):
        self.key = key
        self.next = None


class DoubleLinkNode:
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def search(self,key):
        x = self.head
        while x != None and x.key != key:
            x = x.next
        return x

    def insert(self,x):
        x.next = self.head
        if self.head != None:
            self.head.prev = x
        self.head = x
        x.prev = None

    def delete(self,x):
        if x.prev != None:
            x.prev.next = x.next
        else:
            self.head = x.next
        if x.next != None:
            x.next.prev = x.prev


# circular is a doubly linked list with a sentinel
class CircularDoubleList:
    def __init__(self):
        self.nil = DoubleLinkNode(None)
        self.nil.next = self.nil
        self.nil.prev = self.nil

    def search(self,key):
        x = self.nil.next
        while x != self.nil and x.key != key:
            x = x.next
        return x

    def insert(self,x):
        x.next = self.nil.next
        self.nil.next.prev = x
        self.nil.next = x
        x.prev = self.nil

    def delete(self,x):
        x.prev.next = x.next
        x.next.prev = x.prev


class SingleLinkList:
    def __init__(self):
        self.head = None
        self.end = None
    def search(self,key):
        x = self.head
        while x != None and x.key != key:
            x = x.next
        return x

    def insert(self,x):
        if self.end == None:
            self.end = x
        x.next = self.head
        self.head = x

    def delete(self,x):
        if self.head == x:
            self.head = x.next
            return
        y = self.head
        while y.next != x:
            y = y.next
        y.next = x.next


    def empty(self):
        if self.head == None:
            return True
        return False

    def reverse(self):
        x = self.head
        if x.next == None:
            return

        y = x.next
        x.next = None
        while y != None:
            temp = y.next
            y.next = x
            x = y
            y = temp
        self.head = x




if __name__ == "__main__":

    # doublelist = DoubleLinkedList()
    # for i in range(13):
    #     doublelist.insert(DoubleLinkNode(i))
    #
    # x = doublelist.search(8)
    # doublelist.delete(x)
    # y = doublelist.head
    # while y!= None:
    #     print(y.key)
    #     y = y.next

    # circulardoublelist = CircularDoubleList()
    # for i in range(13):
    #     circulardoublelist.insert(DoubleLinkNode(i))
    # x = circulardoublelist.search(8)
    # print(x.key)
    # circulardoublelist.delete(x)
    # x = circulardoublelist.nil
    # for i in range(13):
    #     print(x.key)
    #     x = x.next

    singlelist = SingleLinkList()

    # singlelist.insert(LinkNode(1))

    # x = singlelist.head
    # print(singlelist.empty())
    # singlelist.delete(x)
    # print(singlelist.empty())


    for i in range(13):
        singlelist.insert(LinkNode(i))

    x = singlelist.search(9)
    y = singlelist.search(8)

    singlelist.delete(x)
    singlelist.delete(y)

    singlelist.reverse()
    z = singlelist.head


    while z!= None:
        print(z.key)
        z = z.next





