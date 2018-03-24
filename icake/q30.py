# Write an efficient function that checks whether any 
# permutation of an input string is a palindrome.

# Examples:

# "civic" should return True
# "ivicc" should return True
# "civil" should return False
# "livci" should return False

def is_palindrome(text):
    """
    Returns True if the given text is a palindrome in any permutation
    else False
    """

    # Property of a palindrome:
    # There be a maximum of only one letter that sums to an odd number
   
    char_count = {}
    # edge cases
    # Consider empty text as palindrome
    
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    odd_count = 0
    for count in char_count.values():
        if count % 2 == 1:
            odd_count += 1
            if odd_count > 1:
                return False
    
    return True

# This solution can be slighlty optimized by using set()
# instead of dictionary and keep track of only the odd
# numbered characters in the given text. Add/Remove operation
# on a set is equivalent to set/del in dict. In terms
# of complexity, the average case is O(1). The overhead
# from using dictionary here isn't much since the sample
# size is somewhat limited based on the char set (ASCII
# or Unicode)