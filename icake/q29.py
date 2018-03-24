# Let's say:

# '(', '{', '[' are called "openers."
# ')', '}', ']' are called "closers."
# Write an efficient function that tells us whether or not an 
# input string's openers and closers are properly nested.

# Examples:

# "{ [ ] ( ) }" should return True
# "{ [ ( ] ) }" should return False
# "{ [ }" should return False

def is_nested(text):
    openers = ['(', '{', '[']
    closers = [')', '}', ']']

    # corner cases
    # text with odd length 
    # empty text

    stack = []
    for char in text:
        if char in openers:
            stack.append(char)
        elif char in closers:
            if stack: # if stack is not empty
                last_opener = stack.pop()
                if closers.index(char) != openers.index(last_opener):
                    return False
            else:
                break

    return len(stack) == 0

    # TODO
    # find complexity of len() function
    # find complexity of comparing a  list to [] versus calling length
    # look into set and frozenset

    
