# Given a list of integers, find the highest product you
# can get from three of the integers.

def get_highest_product_of_three(nums):
    # Can't calculate highest product of 3 with less than 3 numbers
    if len(nums) < 3:
        raise ValueError("Expected a minimum of 3 numbers")
    
    highest_product_of_three = nums[0] * nums[1] * nums[2]
    highest_product_of_two = nums[0] * nums[1]
    highest = max(nums[0], nums[1])
    lowest_product_of_two = nums[0] * nums[1]
    lowest = min(nums[0], nums[1])

    # walk from the third number in the list.
    for n in nums[2:]:
        highest_product_of_three = max(highest_product_of_three,
                                        highest_product_of_two * n,
                                        lowest_product_of_two * n)
        highest_product_of_two = max(highest_product_of_two, highest * n, lowest * n)
        highest = max(highest, n)
        lowest_product_of_two = min(lowest_product_of_two, highest * n, lowest * n)
        lowest = min(lowest, n)
    
    return highest_product_of_three