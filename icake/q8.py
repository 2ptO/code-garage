# Treat a tree as super balanced if the difference between any two leaf nodes
# is not more than 1. Find whether a given binary tree is balanced or not.

class Node:
    def __init__(self, value, left = None, right = None):
        self.left = left
        self.right = right
        self.value = value
    
    def is_leaf(self):
        return self.left is None and self.right is None

def is_super_balanced(root, use_recursion=False):
    if use_recursion:
        return is_balanced_using_recursion(root)
    else:
        return is_balanced_using_iteration(root)

def is_balanced_using_recursion(root):
    if root is None:
        # Treat a null tree as balanced
        return True

    def collect_min_max_depth(node, depth, min_max):
        if node is not None:
            collect_min_max_depth(node.left, depth+1, min_max)
            if node.left == None and node.right == None:
                if depth < min_max[0]:
                    min_max[0] = depth
                if depth > min_max[1]:
                    min_max[1] = depth
            collect_min_max_depth(node.right, depth+1, min_max)
    
    min_max = [float('inf'), -1]
    collect_min_max_depth(root, 1, min_max)
    return (abs(min_max[1] - min_max[0]) <= 1)

def is_balanced_using_iteration(root):
    if root is None:
        return True
    
    # Do a pre-order traversal
    nodes = [(root, 1)]
    depths = []
    while len(nodes) > 0:
        node, depth = nodes.pop()

        if node.is_leaf():
            if depth not in depths:
                depths.append(depth)

            if len(depths) > 2 or \
                (len(depths) == 2 and abs(depths[1] - depths[0])) > 1:
                return False

        if node.right:
            nodes.append((node.right, depth+1))
        if node.left:
            nodes.append((node.left, depth+1))  
    
    return True

# My takeaway
# This property "super balanced" mentioned in the question
# sounds controversial to me. It doesn't consider tree with single
# leaf node or two leaves at same depth to be unbalanced, unlike
# typical balanced tree. 
# 
# I solved it using recursion first, and then using iteration.
# Both solution uses depth first traversal. O(n) time and space.

