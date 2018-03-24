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
    """
    Returns True if the given text has proper nested blocks
    """
    opener_to_closer = {
        '{' : '}',
        '(' : ')',
        '[' : ']'
    }

     # Initially used a list here, and compared the indexes
     # to map openers to closers. Then came to know about
     # set/frozenset classes. Addl tip: dict.keys() and
     # dict.values() returns a dictview objects that are
     # view to the actual keys and values. Change in dict
     # keys/values will impact the objects points to 
     # dict.keys() and dict.values() as well.
    openers = frozenset(opener_to_closer.keys())
    closers = frozenset(opener_to_closer.values())

    openers_stack = []
    for char in text:
        if char in openers:
            openers_stack.append(char)
        elif char in closers:
            if not openers_stack:
                # Found a closer without a opener
                return False

            last_opener = openers_stack.pop()
            if char != opener_to_closer[last_opener]:
                # current closer and last opener didn't match.
                # So, text is not properly nested
                return False

    # If the text is properly nested, openers stack must be empty
    # after completing the walk.
    return len(openers_stack) == 0