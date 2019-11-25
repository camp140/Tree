class node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = None if left is None else left
        self.right = None if right is None else right

    def __str__(self):
        return str(self.data)

    def getData(self):  # accessor
        return self.data

    def getLeft(self):  # accessor
        return self.left

    def getRight(self):  # accessor
        return self.right

    def setData(self, data):  # mutator
        self.data = data

    def setLeft(self, left):  # mutator
        self.left = left

    def setRight(self, right):  # mutator
        self.right = right


class BST:
    def __init__(self, root=None):
        self.root = None if root is None else root

    def addI(self, data):
        if self.root is None:
            self.root = node(data)
        else:
            fp = None  # father of p
            p = self.root  # start comparing from root
            while p:  # while p is not None
                fp = p
                p = p.left if data < p.data else p.right
            if data < fp.data:
                fp.left = node(data)
            else:
                fp.right = node(data)

    def add(self, data):
        self.root = BST._add(self.root, data)

    def _add(root, data):  # recursive _add
        if root is None:
            return node(data)
        else:
            if data < root.data:
                root.left = BST._add(root.left, data)
            else:
                root.right = BST._add(root.right, data)
        return root

    def inOrder(self):
        BST._inOrder(self.root)
        print()

    def _inOrder(root):
        if root:  # if root is not None
            BST._inOrder(root.left)
            print(root.data, end=' ')
            BST._inOrder(root.right)

    def printSideway(self):
        return BST._printSideway(self.root, 0)

    def _printSideway(root, level):
        if root:  # if root is not None
            BST._printSideway(root.right, level + 1)
            print('   ' * level, root.data)
            BST._printSideway(root.left, level + 1)

    def preOrder(self):
        BST._preOrder(self.root)
        print()

    def _preOrder(root):
        if root:  # if root is not None
            print(root.data, end=' ')
            BST._preOrder(root.left)
            BST._preOrder(root.right)

    def postOrder(self):
        BST._postOrder(self.root)
        print()

    def _postOrder(root):
        if root:  # if root is not None
            BST._postOrder(root.left)
            BST._postOrder(root.right)
            print(root.data, end=' ')

    def search(self, data):
        return BST._search(self.root, data)

    def _search(root, data):
        if root:
            if data < root.data:
                return BST._search(root.left, data)
            elif data > root.data:
                return BST._search(root.right, data)
            else:
                return root
        else:
            return None

    def path(self, data):
        return BST._path(self.root, data)

    def _path(root, data):
        if root:
            if root.data == data:
                print(root.data)
            else:
                print(root.data, " -> ", end=" ")
                if data > root.data:
                    BST._path(root.right, data)
                else:
                    BST._path(root.left, data)

    def delete(self, data):
        return BST._delete(self.root, data)

    def _delete(root, data):
        if root is not None:
            if data < root.data:
                root.left = BST._delete(root.left, data)
            elif data > root.data:
                root.right = BST._delete(root.right, data)
            #found specified Node:
            else:
                #Node with one or no child:
                if root.right is None:
                    temp = root.left
                    root = None
                    return temp
                elif root.left is None:
                    temp = root.right
                    root = None
                    return temp

                #Node with two children:
                else:
                    temp = BST.getSuccessor(root.right) #smallest right
                    root.data = temp.data #copy here
                    root.right = BST._delete(root.right, temp.data) #delete copied node
            return root

    def getSuccessor(root):
        if root:
            if root.left != None:
                return BST.getSuccessor(root.left)
            else:
                return root

# 14 4 9 7 15 3 18 16 20 5 16
l = [int(i) for i in input("Input: ").split()]
print(l)

tree = BST()
for element in l:
    tree.addI(element)

print("Print InOrder: ")
tree.inOrder()
print("Print PreOrder: ")
tree.preOrder()
print("Print PostOrder: ")
tree.postOrder()

print("Print Sideway: ")
tree.printSideway()

print("Search: ", tree.search(15))

print("Path: ", end=' ')
tree.path(5)

tree.delete(5)
tree.printSideway()
