# We have our lists of orders sorted numerically already, in lists. 
# Write a function to merge our lists of orders into one sorted list.

from collections import deque

def merge_sorted_lists_using_deque(left, right):
    """ Merge two sorted lists using a deque. Modifies the input lists"""

    # Edge cases
    if not left and not right:
        return []
    
    if left and not right:
        return left
    
    if not left and right:
        return right

    merged = deque()

    while (len(left) > 0 and len(right) > 0):
        left_item = left.pop()
        right_item = right.pop()

        min_item = min(left_item, right_item)
        max_item = max(left_item, right_item)

        maxlist = left if max_item == left_item else right
        # minlist = left if maxlist == right else right

        # Enqueue the max into the merged list
        merged.appendleft(max_item)

        while (len(maxlist) > 0 and maxlist[-1] > min_item):
            merged.appendleft(maxlist.pop())
        
        merged.appendleft(min_item)
    
    # Add remaining items from non-empty list
    assert (len(left) == 0 or len(right) == 0)
    for i in range(len(left)-1, -1, -1):
        merged.appendleft(left[i])
    for i in range(len(right)-1, -1, -1):
        merged.appendleft(right[i])
    
    return merged

def merge_sorted_lists(left, right):
    """ Merge two sorted lists"""
    # Edge cases
    if not left and not right:
        return []
    
    if left and not right:
        return left
    
    if not left and right:
        return right

    merged = []

    left_index = 0
    right_index = 0
    left_max = len(left)
    right_max = len(right)

    # Loop until neither list is empty
    while (left_index < left_max and right_index < right_max):
        
        max_item = max(left[left_index], right[right_index])
        # Add items from the min list
        if left[left_index] < right[right_index]:
            while (left_index < left_max and left[left_index] < right[right_index]):
                merged.append(left[left_index])
                left_index += 1
            right_index += 1
        else:
            while (right_index < right_max and right[right_index] < left[left_index]):
                merged.append(right[right_index])
                right_index += 1
            left_index += 1
        
        merged.append(max_item)
    
    # Add remaining items from non-empty list
    for i in range(left_index, left_max):
        merged.append(left[i])
    for i in range(right_index, right_max):
        merged.append(right[i])
    
    return merged

# I worked out fully on paper this time, then ported the algorithm
# into actual code. The key logic is same as the solution described
# in the original problem, but steps in mine are slightly different
# because they are adapted from my handsolved solution. The solution
# above may show multiple loops, but essentially it is O(n) because
# we don't walk the left and right list more than once.
# Worked out the solution with deque first, it was easy to code but
# modified the input lists. So switched to the second based on lists.
# Learnt few extra information in this exercise: Python sort uses
# Timsort which is optimized to sort lists with sorted sublists.
# In built mergesort is available from heapq module.(heapq.merge())
# Another optimization could be to use generator to avoid storing
# the merged list in memory. 
