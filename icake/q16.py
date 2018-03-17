# Write a function max_duffel_bag_value() that takes a list of cake type tuples
# and a weight capacity, and returns the maximum monetary value the duffel bag 
# can hold.

def max_duffel_bag_value_sub_optimal(cakes, capacity):
    """
    Given a list of cake tuples with weight and price, returns maximum
    monetary possible within the capacity limit.
    """
    
    # Pseudocode
    # sort by maximum value
    # max_value = lowest weight, highest price -> price/weight ratio must be higher
    # sort by highest price/weight ratio to lowest
    # starting from max value cake, add as much as possible
    # if capacity exceeded, add the second valuable cake as much as possible
    # so on and so forth
    
    if not cakes or not capacity:
        # Empty cake list or bag has no capacity.
        # No actual monetary value
        return 0

    try:
        cakes_sorted_by_value = sorted(cakes, key=lambda x: x[1]/x[0], reverse=True)
    except(ZeroDivisionError):
        raise ValueError("Cannot hold infinite weight of a cake")

    max_value = 0
    for cake_weight, cake_price in cakes_sorted_by_value:
        max_num_of_this_cake = int(capacity/cake_weight)
        max_value += max_num_of_this_cake * cake_price
        if capacity % cake_weight == 0:
            # we have perfect numbers of this cake to pack
            # or, no capacity left
            break
        else:
            # not a perfect num. So reduce the capacity by
            # the number of times the cake was packed
            capacity -= (max_num_of_this_cake * cake_weight)
    return max_value

    