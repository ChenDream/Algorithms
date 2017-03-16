
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
    def insert(self,key):
        node = Node(key)
        if self.root == None:
            self.root = node
            return
