# Write a function for finding the index of the "rotation point," in a 
# given list of words

# e.g.
#   words = [
#     'ptolemaic',
#     'retrograde',
#     'supplant',
#     'undulate',
#     'xenoepist',
#     'asymptote',  # <-- rotates here!
#     'babka',
#     'banoffee',
#     'engender',
#     'karpatka',
#     'othellolagkage',
# ]

def find_rotation_point(words):
    """ 
    Returns the word at the index of rotating point if there is rotation.
    else None. Assumes one or no rotation point
    """
    if not words:
        return None
    
    if len(words) == 1:
        # Only one word in the list. Consider that as the rotation point.
        return words[0]
    
    floor = 0
    ceiling = len(words) - 1
    first_word = words[0]

    # floor may never go above ceiling return before floor reach ceiling. 
    # But having this check as a precaution against accessing out of range
    while (floor < ceiling):
        guess = int(floor + (ceiling - floor)/2)
        print(guess)
        if words[guess] >= first_word:
            floor = guess
        else:
            ceiling = guess
        if floor + 1 == ceiling:
            # We are down to two elements
            if words[floor] > words[ceiling]:
                return words[ceiling]
            else:
                return None

    return None

# This is a slightly modified form of binary search
# I first assumed that the list is infinite and there may be multiple
# rotation point within the list. So used divide and conquer method
# with recursion initially. Then read the question again, understood
# the constraints and used the iterative method.
# Tip: With binary search, usually we have some value to find. If the
# value to be find is not given, guess it (for e.g. middle index)
            