# Write a function get_products_of_all_ints_except_at_index()
# that takes a list of integers and returns a list of the products.
# Given [1, 7, 3, 4] , result should be [84, 12, 28, 21]

# My answers
# I started with brute force method, walked through the inputs
# in two loops, leading to O(n^2). On expanding the example
# and writing down different levels of the problem, a pattern
# started to emerge. at each index, the result is the product
# of all numbers before that index and after that index. 
# With that approach, this problem can be solved in O(n) time
# and O(n) space. 

# My take
# Break into subproblems
# Identify if any pattern
# Go greedy in saving the results of the subproblems
# If stuck, work out with a different example
# Test boundary conditions
# Optimize for time and space

def get_products_of_all_ints_except_at_index(input_nums):
    if len(input_nums) <= 1:
        # Can be considered as error condition too.
        return input_nums
    prod_of_all_ints_except_at_index = [None] * len(input_nums)
    product_so_far = 1
    
    # Walk from the first to last.

    # Tip: range in Python3 does what xrange typically does.
    # No xrange functionality in Python3
    for i in range(len(input_nums)):
        prod_of_all_ints_except_at_index[i] = product_so_far
        product_so_far *= input_nums[i]
    
    # Walk from the last to first.
    product_so_far = 1
    for i in range(len(input_nums)-1, -1, -1):
        prod_of_all_ints_except_at_index[i] *= product_so_far
        product_so_far *= input_nums[i]

    return prod_of_all_ints_except_at_index
    
