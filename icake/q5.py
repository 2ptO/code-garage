# Write a function that, given:

# an amount of money
# a list of coin denominations
# computes the number of ways to make the amount of money with coins of the available denominations.

# Example: Given 4 cents to change, and coins [1, 2, 3], there are 4 ways to make change
# [1, 1, 1, 1]
# [1, 1, 2]
# [1, 3]
# [2 ,2]
#
# This is a classic example of dynamic programming problem. I first struggled
# find the answer on my own. I took hints and even looked at the full solution,
# but didn't understand what was going. I spent more time working out examples
# step by step multiple times. That helped a lot in developing the intuition
# required to understand this problem. After working through the problem set,
# I came up with my own solution with multiple versions (top-down, top-down-optimized
# and bottom-up). The top-down version uses recursion while the bottom-up
# uses dynamic programming.

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