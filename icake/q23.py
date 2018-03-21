# Write a function contains_cycle() that takes the first node in a singly-linked list
# and returns a boolean indicating whether the list contains a cycle.
# Skipped Q22 which was a simple question on link list.
#
class LinkedListNode:
    """
    Simple linked list class
    """
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

def contains_cycle(head):
    """
    Return true if the list pointed by head contains a cycle
    """
    if head is None:
        # Consider no cycle if there is no head node
        return False
    
    first = head
    second = head
    while (second is not None and second.next_node is not None):
        first = first.next_node
        second = second.next_node.next_node
        if first == second:
            return True
    
    return False

