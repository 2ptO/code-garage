import time

# Dynamic Programming Python implementation of Coin 
# Change problem
def count(list_of_coins, change_to_make):
    # We need n+1 rows as the table is constructed 
    # in bottom up manner using the base case 0 value
    # case (n = 0)
    no_of_coins = len(list_of_coins)
    # table = [[0 for x in range(m)] for x in range(change_to_make+1)]
    # table = [[0 for x in range(change_to_make+1)] for x in range(no_of_coins)]
    table = [[0 for x in range(change_to_make+1)] for x in range(no_of_coins)]

    # Fill the base case
    for i in range(len(table)):
        table[i][0] = 1

    # Fill rest of the table entries in bottom up manner

    for j in range(no_of_coins):
        for change in range(1, change_to_make+1):
            current_coin = list_of_coins[j]
            combinations_with_current_coin = 0
            combinations_without_current_coin = 0

            if (change - current_coin) >= 0:
                combinations_with_current_coin = table[j][change - current_coin]
            
            # Count of solutions excluding S[j]
            if j >= 1:
                combinations_without_current_coin = table[j-1][change]

            # total count
            table[j][change] = combinations_with_current_coin + combinations_without_current_coin
            print("current coin = ", list_of_coins[:j+1], "change = ", change)
            for row in table:
                print(row)
            # time.sleep(1)

    return table[no_of_coins-1][change_to_make]

def make_change(coins, given_change):
    assert given_change > 0
    change_table = [0 for x in range(given_change+1)]
    change_table[0] = 1
    for current_coin in coins:
        for current_change in range(1, given_change+1):
            if current_change >= current_coin:
                change_table[current_change] += change_table[current_change-current_coin]
        print(change_table)
    return change_table[-1]

def make_change_internal(coins, index, change):
    if change == 0:
        return 1
    if index >= len(coins) or change < 0:
        return 0
    current_coin = coins[index]
    print(f'change: {change} coins: {coins[index:]}')
    n_ways = 0
    while change >= 0:
        n_ways += make_change_internal(coins, index+1, change)
        change -= current_coin
    return n_ways
    
def make_change_recursive(coins, given_change):
    return make_change_internal(coins, 0, given_change)

# Driver program to test above function
arr = [1, 2, 3, 2]
m = len(arr)
n = 4
print("Final answer = ", count(arr, n))

print("Answer using my method = ", make_change(arr, n))

print("Answer using my recursive = ", make_change_recursive(arr, n))

# This code is contributed by Bhavya Jain
