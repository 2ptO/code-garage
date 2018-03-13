# Write a function to check that a binary tree is a valid binary search tree

class BTNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def traverse_in_order(node):
    if node:
        yield from traverse_in_order(node.left)
        yield node.value
        yield from traverse_in_order(node.right)

def is_binary_search_tree(root):
    max_value = -float('inf')
    for value in traverse_in_order(root):
        if value > max_value:
            max_value = value
        else:
            return False
    return True

# My takeaway
# Multiple solutions seem to be available for this problem.
# I chose the traversal method since it occurred to me intuitively.
# I first thought about storing the sorted list returned by
# in-order traversal. Looking for ways to optimize, it turned out
# all we need is to ensure that value to be added into the sorted list
# is higher than the previous high in the list. So if we keep track
# of previous maximum, that should suffice here. DFS seems to be a
# better choice here because 1) tree could be unbalanced 2) extra
# level of breadth search could double the number of nodes searched
# Python generators came in handy here. Otherway is to embed the check
# for previous max within the traversal function itself by passing it
# as extra parameter. 
# 
# Other solution is using topdown approach where root value is passed
# down the tree - at each node, we check for the following condition:
# node.value is less than all of nodes that are its left ancestors
# node.value is higher than all of nodes that are its right ancestors