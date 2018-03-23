# Write a function kth_to_last_node() that takes an integer kk and the 
# head_node of a singly-linked list, and returns the kth to last node in the list.

class LinkedListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
def kth_to_last_node(head, k):
    """
    Return the kth node from the end of the list
    Returns None if k is greater than the length of the list
    """ 
    if k < 0:
        raise ValueError("k value must be positive")
    
    kth = None
    last = head
    i = 0
    while (i < k and last != None):
        last = last.next
        i += 1
    
    if last: # we haven't gone past the last node, so good to go further
        # move kth and last pointer one step at a time until the last
        # node arrives
        kth = head
        while last.next:
            last = last.next
            kth = kth.next
        return kth
    
    return kth

# I came up with three solutions this time. 
# first with super simple stack based solution, then walking the list twice,
# and finally with single walk method. I slipped a little when converting
# my algo into code. Have to be more careful with that.
# This is a good example where a solution capitalizes processors LRU caching
# Many items in the list is walked twice, so there is good chance to
# benefit from memory caching.
        
        

