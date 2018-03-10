# Write a function that, given:

# an amount of money
# a list of coin denominations
# computes the number of ways to make the amount of money with coins of the available denominations.

# Example: Given 4 cents to change, and coins [1, 2, 3], there are 4 ways to make change
# [1, 1, 1, 1]
# [1, 1, 2]
# [1, 3]
# [2 ,2]]

def make_change_top_down(change, coins):
    return _make_change_top_down_recursive(change, coins, 0)

def _make_change_top_down_recursive(change, coins, index):
    # Working through the examples step by step, I found the conditions
    # for base cases at the bottom most step in each iteration.
    # Base cases:
    if change == 0:
        # no change left, either we found a perfect coin.
        # Other way to think this case: How many ways one can make a change of 0?
        # This forms the very basic intuition in bottom up approach too.
        return 1
    
    if index >= len(coins) or change < 0:
        # We are out of coins!
        return 0
    
    current_coin = coins[index]
    n_ways = 0
    while (change >= 0):
        # For number of times you can make change with current coin,
        # find if you can make change for the remaining amount with
        # the remaining coins
        n_ways += _make_change_top_down_recursive(change, coins, index+1)
        change -= current_coin
    return n_ways

def make_change_bottom_up_v1(change, coins):
    """
    Bottom up solution for coin change problem, using two dimensional array
    A row of change values for each coin.
    """
    change_table = [[0 for x in range(change+1)] for x in range(len(coins))]

    # Initialize the base case of having no change for each coin.
    for row in change_table:
        row[0] = 1
    
    for i in range(len(coins)):
        for amount in range(1, change+1):
            current_coin = coins[i]

            # Can make change for amount X with a coin only if the
            # amount is higher than the coin itself.
            nways_with_current_coin = change_table[i][amount-current_coin] \
                                        if (amount - current_coin) >= 0 else 0
            
            # Can lookup the table for previous coin only if we have gone
            # past the first coin in our list
            nways_without_current_coin = change_table[i-1][amount] if i >= 1 else 0
            
            change_table[i][amount] = nways_with_current_coin + nways_without_current_coin

    return change_table[len(coins)-1][change]
    # Sample table built for change 5 with coins [1, 2, 3, 4]
    # When coin = 1
    # [1, 1, 1, 1, 1, 1]
    # [1, 0, 0, 0, 0, 0]
    # [1, 0, 0, 0, 0, 0]
    # [1, 0, 0, 0, 0, 0]
    # Coin = [1, 2]
    # [1, 1, 1, 1, 1, 1]
    # [1, 1, 2, 2, 3, 3]
    # [1, 0, 0, 0, 0, 0]
    # [1, 0, 0, 0, 0, 0]

    # Coin = [1, 2, 3]
    # [1, 1, 1, 1, 1, 1]
    # [1, 1, 2, 2, 3, 3]
    # [1, 1, 2, 3, 4, 5]
    # [1, 0, 0, 0, 0, 0]

    # Coin = [1, 2, 3, 4]
    # [1, 1, 1, 1, 1, 1]
    # [1, 1, 2, 2, 3, 3]
    # [1, 1, 2, 3, 4, 5]
    # [1, 1, 2, 3, 5, 6]


def make_change_bottom_up_v2(change, coins):
    """
    Bottom up solution for coin change problem, but using an
    one dimensional array. 
    """
    # make_change_bottom_up_v1 used a two dimensional array to keep track
    # of the change values at each iteration. If you look at how the
    # nways_without_current_coin value is obtain in each iteration, it is
    # nothing but value in the same cell prior to modification. So we can
    # avoid using an extra row of memory for each coin and instead overwrite
    # the existing values itself.

    change_table = [0 for x in range(change+1)]

    # base of having no change.
    change_table[0] = 1

    for coin in coins:
        for amount in range(1, change+1):
            if amount - coin >= 0:
                change_table[amount] += change_table[amount - coin]

    return change_table[change]
    # Table values after each iteration for change amount 5, coins [1, 2, 3, 4]
    # 
    # Coin: 1 table: [1, 1, 1, 1, 1, 1]
    # Coin: 2 table: [1, 1, 2, 2, 3, 3]
    # Coin: 3 table: [1, 1, 2, 3, 4, 5]
    # Coin: 4 table: [1, 1, 2, 3, 5, 6]
    # 
    # Compare this table with the table from solution v1 with two dimensional table

# This is a classic example of dynamic programming problem. I first struggled
# find the answer on my own. I took hints and even looked at the full solution,
# but didn't understand what was going. I spent more time working out examples
# step by step multiple times. That helped a lot in developing the intuition
# required to understand this problem. After working through the problem set,
# I came up with my own solution with multiple versions (top-down, top-down-optimized
# and bottom-up). The top-down version uses recursion while the bottom-up
# uses dynamic programming. 
# All of these solutions run in O(n*c) complexities, where n is the number of
# coins and m is change amount. Starting with the top down solution first 
# helped me to understand the problem, break into subproblems and eventually
# into solving it from botton up. 