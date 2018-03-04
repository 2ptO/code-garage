class Node: # Is object really needed? What is the significance?
    def __init__(self, value, parent = None, leftChild = None, rightChild = None):
        self.value = value
        self.left = leftChild
        self.right = rightChild
        self.parent = parent
    
    def has_left_child(self):
        return self.left is not None
    
    def has_right_child(self):
        return self.right is not None
    
    def has_parent(self):
        return self.parent is not None
    
    def is_root(self):
        return self.parent is None
    
    def has_no_children(self):
        return (not (self.has_left_child() or self.has_right_child()))
    
    def has_one_child(self):
        return (self.left and not self.right) or (self.right and not self.left)
    
    def has_both_children(self):
        return (self.has_left_child() and self.has_right_child())
    
    def is_left_child(self):
        return self.has_parent() and self.parent.left == self
    
    def is_right_child(self):
        return self.has_parent() and self.parent.right == self
    
    def get_height(self):
        if self.has_no_children():
            return 1
        left_height = self.left.get_height() if self.has_left_child() else 0
        right_height = self.right.get_height() if self.has_right_child() else 0
        return max(left_height, right_height) + 1
    
    def find_min(self):
        while (self.has_left_child()):
            return self.left.find_min()
        return self
        # Iterative solution:
        # if not self.has_left_child():
        #     return self
        
        # left = self.left
        # while (left is not None):
        #     left = self.left
        # return left

    def find_max(self):
        while (self.has_right_child()):
            return self.right.find_max()
        return self
    
    def replace_data(self, new_val, new_left, new_right):
        self.value = new_val
        self.left = new_left
        self.right = new_right
        if self.has_left_child():
            self.left.parent = self
        if self.has_right_child():
            self.right.parent = self
    
    def find_successor(self):
        # Successor is the next highest node of the current node.
        successor = None
        if self.has_right_child():
            successor = self.right.find_min()
        else:
            if self.has_parent():
                if self.is_left_child():
                    successor = self.parent
                else:
                    # node has no right child and is the right child of its parent
                    # its successor is the sucessor of its parent without this node
                    self.parent.right = None
                    successor = self.parent.find_successor()
                    self.parent.right = self
        return successor
    
    def detach(self):
        if self.has_no_children():
            if self.is_left_child():
                self.parent.left = None
            else:
                self.parent.right = None
        elif self.has_one_child():
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left = self.left
                else:
                    self.parent.right = self.left
                self.left.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
                self.right.parent = self.parent
        else:
            raise AssertionError("Not a leaf node")

class BinarySearchTree:
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
    
    def find(self, value):
        if self.root is None:
            return None
        return self._find(self.root, value)
        
    def _find(self, node, value):
        if node is None:
            return None
        elif value == node.value:
            return node
        elif value < node.value:
            return self._find(node.left, value)
        else:
            return self._find(node.right, value)

    def delete(self, value):
        node_to_delete = self.find(value)
        if node_to_delete is None:
            raise KeyError
        if node_to_delete == self.root and node_to_delete.has_no_children():
            self.root = None
            self.node_count = 0
        else:
            self._delete(node_to_delete)
            self.node_count -= 1
    
    def _delete(self, node):
        if node.has_no_children():
            if node.is_left_child():
                node.parent.left = None
            else:
                node.parent.right = None
            # root-only case is handled in delete() itself.
        elif node.has_one_child():
            if node.has_left_child():
                if node.is_left_child():
                    node.parent.left = node.left
                    node.left.parent = node.parent
                elif node.is_right_child():
                    node.parent.right = node.left
                    node.left.parent = node.parent
                else:
                    # Root node. Just replace the node contents
                    node.replace_data(node.left.value, node.left.left, node.left.right)
            else:
                if node.is_left_child():
                    node.parent.left = node.right
                    node.right.parent = node.parent
                elif node.is_right_child():
                    node.parent.right = node.right
                    node.right.parent = node.parent
                else:
                    # Root node. Just replace the node contents
                    node.replace_data(node.right.value, node.right.left, node.right.right)
        else:
            # Node has both left and right child.
            successor = node.find_successor()
            successor.detach()
            node.value = successor.value
    
    def get_values_in_order(self):
        values_in_order = []
        self._iterate_in_order(self.root, values_in_order)
        return values_in_order
    
    def _iterate_in_order(self, node, values_in_order):
        if node != None:
            self._iterate_in_order(node.left, values_in_order)
            values_in_order.append(node.value)
            self._iterate_in_order(node.right, values_in_order)
    
    def get_height(self):
        return self.root.get_height() if self.root != None else 0
    
    def get_min(self):
        if self.root is not None:
            return self.root.find_min().value
        raise IndexError
    
    def get_max(self):
        if self.root is not None:
            return self.root.find_max().value
        raise IndexError
    
    
