import random
from DataStructures.Stacks import Stack
class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

class BinaryTree:
    def __init__(self):
        self.root =None
        self.count = 0
    # random insert
    def randomInsert(self,key):
        node = Node(key)
        self.count +=1
        if self.root == None:
            self.root = node
            return
        leaf = self.root
        while True:
            r = random.randint(1,2)
            if r == 1 and leaf.left == None:
                node.parent = leaf
                leaf.left = node
                break
            elif r == 1:
                leaf = leaf.left
            elif r == 2 and leaf.right == None:
                node.parent = leaf
                leaf.right = node
                break
            else:
                leaf = leaf.right

    def getNodes(self,type="r"):
        if type == "r":
            self.printAllNode_recursive(self.root)
        elif type == "n1":
            self.printAllNode_Nonrecursive()
        else:
            self.printAllNode_Nonrecursive_2()

    def printAllNode_recursive(self,node):
        if node == None:
            return
        print(node.key)
        self.printAllNode_recursive(node.left)
        self.printAllNode_recursive(node.right)

    def printAllNode_Nonrecursive(self):
        node = self.root
        if node == None:
            return
        stack = Stack(self.count)
        stack.push(node)
        while not stack.empty():
            node = stack.pop()
            print(node.key)
            if node.left != None:
                stack.push(node.left)
            if node.right != None:
                stack.push(node.right)
    # no more than constance extra space, no modify tree
    def printAllNode_Nonrecursive_2(self):
        # need to fix some logic error
        # current,before = self.root,None
        # if current == None:
        #     return
        # while current != None:
        #     print(current.key)
        #     if current.left == None and current.right == None:
        #         current,before = current.parent,current
        #     else:
        #         if before == current.left:
        #             current,before = current.right,current
        #         if before == current.right:
        #             current,before = current.parent,current
        #         if before == current.parent:
        #             current,before = current.left,current
        return
# unbounded branch tree is a tree with unlimited children
class UnboundedBranchTree:
    def __init__(self):
        self.root = None

    def randomInsert(self,key):
        node = Node(key)
        if self.root == None:
            self.root = node
            return
        leaf = self.root
        # root can not have right sibling children
        if leaf.left == None:
            node.parent = leaf
            leaf.left = node
            return

        # root's left children
        leaf = leaf.left
        while True:
            # 1, go to left node, 2 to go right sibling
            r = random.randint(1,2)
            if r == 1 and leaf.left == None:
                node.parent = leaf
                leaf.left = node
                break
            elif r == 1:
                leaf = leaf.left
            elif r == 2 and leaf.right == None:
                # different to binary tree
                node.parent = leaf.parent
                leaf.right = node
                break
            else:
                leaf = leaf.right
    def getNodes(self,type= "r"):
        self.printAllNode_recursive(self.root)
    def printAllNode_recursive(self,node):
        if node == None:
            return
        print(node.key)
        self.printAllNode_recursive(node.left)
        self.printAllNode_recursive(node.right)

if __name__ == "__main__":
    bt = BinaryTree()
    for i in range(13):
        bt.randomInsert(i)
    bt.getNodes("n1")

    # tree = UnboundedBranchTree()
    # for i in range(13):
    #     tree.randomInsert(i)
    # tree.getNodes()

