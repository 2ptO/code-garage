# "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) 
# they get confusing."

# Write a function that, given a sentence like the one above, along with the 
# position of an opening parenthesis, finds the corresponding closing parenthesis.

# Example: if the example string above is input with the number 10 (position 
# of the first parenthesis), the output should be 79 (position of the last parenthesis).

def find_matching_parenthesis(text, open_paranthesis_pos):
    """ 
    Return the position of the matching closing paranthesis for the
    given open paranthesis if match exists else returns -1
    """
    if not 0 <= open_paranthesis_pos < len(text):
        raise ValueError("Invalid value for open_paranthesis_pos")
    
    if text[open_paranthesis_pos] is not '(':
        raise ValueError("Text is missing ( at position {}".format(open_paranthesis_pos))
    
    n_open_ps = 0 # number of open parantheses
    for pos in range(open_paranthesis_pos+1, len(text)):
        if text[pos] is '(':
            n_open_ps += 1
        elif text[pos] is ')':
            n_open_ps -= 1
            if n_open_ps < 0: # first closing paranthesis without a matching open paranthesis
                return pos

    # No matching paranthesis found
    return -1

# solved it with stack first, but then it has an additional space overhead
# Then solved it with alternate method in O(1) space. Both the methods take
# O(n) time.
           
        
