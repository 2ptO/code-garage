# Write a function to find the 2nd largest element in a binary search tree.

class BTNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    # These methods are not really part of the solution as such.
    # Including methods like these make the code cleaner and also
    # refresh my language skills.
    def is_leaf(self):
        return (not self.left and not self.right)
    
    def __eq__(self, value):
        return self.value == value
    
    def __lt__(self, value):
        return self.value < value

    def __gt__(self, value):
        return self.value > value

# Helper functions to insert values into a node
def insert(root, value):
    if root is None:
        raise ValueError("Root is invalid")
    if value > root:
        if root.right is None:
            root.right = BTNode(value)
        else:
            insert(root.right, value)
    elif value < root:
        if root.left is None:
            root.left = BTNode(value)
        else:
            insert(root.left, value)

# Helper function to traverse the nodes during debugging
def traverse(root):
    if root:
        yield from traverse(root.left)
        yield root.value
        yield from traverse(root.right)

def _find_max(root):
    if root is None:
        raise ValueError("Root is invalid")
    node = root
    while node.right:
        node = node.right
    return node.value

def find_second_max(root):
    if root is None:
        raise ValueError("Root is invalid")
    if root.is_leaf():
        raise ValueError("Root needs at least one child")
    
    node = root
    # Go down the tree until a node without right grandchild
    while (node.right and node.right.right):
        node = node.right
    
    if node.right:
        # We are at second most node on the right. The second max
        # can either be this node if its right child has no children
        # or, maximum value of the left subtree of its right child
        if node.right.is_leaf():
            return node.value
        else:
            assert node.right.right is None
            return _find_max(node.right.left)
    else:
        # node has no children on the right. 
        return _find_max(node.left)

# This solution may not be very clean in terms of the code flow.
# I chose to implement this for two reasons: 1. It naturally 
# came to my mind when I tried to solve the problem 2. Runs
# in lesser time (O(log n)) and space (O(1)).