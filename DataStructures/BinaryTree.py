import random
class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

class BinaryTree:
    def __init__(self):
        self.root =None

    # random insert
    def randomInsert(self,key):
        node = Node(key)
        if self.root == None:
            self.root = node
            return
        leaf = self.root
        while leaf != None:
            r = random.randint(1,2)
            if r == 1:
                leaf = leaf.left
            else:
                leaf = leaf.right
        leaf = node

if __name__ == "__main__":
    bt = BinaryTree()
    for i in range(13):
        bt.randomInsert(i)
    print("Done")

