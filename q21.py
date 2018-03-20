# Given the list of IDs, which contains many duplicate integers and
# one unique integer, find the unique integer.
 
def find_unique_number(numbers):
    """
    Finds the unique number in a given list of numbers that
    may have multiple duplicate numbers. Assumes that list
    has only one unique integer and one or more duplicate
    sets of non-unique integers
    """
    # Using the XOR logic to cancel out the duplicate numbers
    # Will work iff the list has one unique number. To find
    # actual frequency, we can use hash table
    xor_sum = 0
    for number in numbers:
        xor_sum ^= number
    
    return xor_sum

