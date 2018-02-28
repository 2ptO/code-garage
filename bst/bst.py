class Node(object): # Is object really needed? What is the significance?
    def __init__(self, value, parent = None, leftChild = None, rightChild = None):
        self.value = value
        self.left = leftChild
        self.right = rightChild
        self.parent = parent
    
    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None
    
    def has_no_children(self):
        return (not self.has_left_child()) and (not self.has_right_child())
    
    def has_both_children(self):
        return (self.has_left_child() and self.has_right_child())
    
    def get_height(self):
        if self.has_no_children():
            return 1
        left_height = self.left.get_height() if self.has_left_child() else 0
        right_height = self.right.get_height() if self.has_right_child() else 0
        return max(left_height, right_height) + 1

class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.node_count = 0
    
    def __len__(self):
        return self.node_count
    
    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
            self.node_count += 1
        else:
            self._insert(self.root, value)
    
    def _insert(self, node, value):
        if value < node.value:
            if node.has_left_child():
                self._insert(node.left, value)
            else:
                node.left = Node(value, node)
                self.node_count += 1                
        elif value > node.value:
            if node.has_right_child():
                self._insert(node.right, value)
            else:
                node.right = Node(value, node)
                self.node_count += 1
        else:
            pass # Value exists already
    
    def get_values_in_order(self):
        values_in_order = []
        self._iterate_in_order(self.root, values_in_order)
        return values_in_order
    
    def _iterate_in_order(self, node, valuesInOrder):
        if node != None:
            self._iterate_in_order(node.left, valuesInOrder)
            valuesInOrder.append(node.value)
            self._iterate_in_order(node.right, valuesInOrder)
    
    def get_height(self):
        return self.root.get_height() if self.root != None else 0
    

