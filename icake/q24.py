# Write a function for reversing a linked list.  Do it in-place.

class LinkedListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

def walk_list(node):
    """
    Traverse the given node list and yields one value at a time
    """
    while (node is not None):
        yield node.value
        node = node.next_node
    
def reverse_list(node):
    """
    Reverse a given list in place and return the new head
    """
    if node is None or node.next_node is None:
        # No node or single node case
        return node
    
    original_head = node
    head = node
    tail = node.next_node
    
    while tail is not None:
        next_tail = tail.next_node

        # Keep moving the original head towards the tail end
        original_head.next_node = next_tail

        # Current tail becomes the new head
        tail.next_node = head
        head = tail

        # Go to next tail
        tail = next_tail
    
    return head


    
