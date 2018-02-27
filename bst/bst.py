class Node(object): # Is object really needed? What is the significance?
    def __init__(self, value, parent = None, leftChild = None, rightChild = None):
        self.value = value
        self.left = leftChild
        self.right = rightChild
        self.parent = parent
    
    def hasLeftChild(self):
        return self.left != None
    
    def hasRightChild(self):
        return self.right != None
    
    def hasNoChildren(self):
        return (not self.hasLeftChild()) and (not self.hasRightChild())
    
    def hasBothChildren(self):
        return (self.hasLeftChild() and self.hasRightChild())
    
    def getHeight(self):
        if self.hasNoChildren():
            return 1
        leftHeight = self.left.getHeight() if self.hasLeftChild() else 0
        rightHeight = self.right.getHeight() if self.hasRightChild() else 0
        return max(leftHeight, rightHeight) + 1

class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.nodeCount = 0
    
    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)
    
    def _insert(self, node, value):
        if value < node.value:
            if node.hasLeftChild():
                self._insert(node.left, value)
            else:
                node.left = Node(value, node)                
        elif value > node.value:
            if node.hasRightChild():
                self._insert(node.right, value)
            else:
                node.right = Node(value, node)
        else:
            pass # Value exists already
    
    def getValuesInOrder(self):
        valuesInOrder = []
        self._inOrder(self.root, valuesInOrder)
        return valuesInOrder
    
    def _inOrder(self, node, valuesInOrder):
        if node != None:
            self._inOrder(node.left, valuesInOrder)
            valuesInOrder.append(node.value)
            self._inOrder(node.right, valuesInOrder)
    
    def getHeight(self):
        return self.root.getHeight() if self.root != None else 0
    

