# Write a function for doing an in-place shuffle of a list.

# The shuffle must be "uniform," meaning each item in the original 
# list must have the same probability of ending up in each spot in the final list.

# Assume that you have a function get_random(floor, ceiling) for getting
# a random integer that is >= floor and <= ceiling.

from random import randint

def shuffle(items):
    if not items:
        return []
    
    for position in range(len(items)-1):
        new_position = randint(position, len(items)-1)
        
        if position != new_position:
            items[position], items[new_position] = items[new_position], items[position]

# Derived this from my previous solution to permutation problem
# In first version, I generated random numbers between position+1 and len-1,
# thinking that that will exclude the current position from the
# sample set for the random positions. However, it ran into a
# risk of accessing out of bounds. Then changed to the current
# version. Learnt that this style of random number generation
# is called Fisher-Yates shuffle. Also, random.randrange() is
# what we usually need often than randint() which includes the
# endpoint as well.
