# Write a recursive function for generating all permutations of an input string. 
# Return them as a set.

# Don't worry about time or space complexity—if we wanted efficiency 
# we'd write an iterative version.

# To start, assume every character in the input string is unique.
# Your function can have loops—it just needs to also be recursive.

def permutations(text):
    perm = set()

    if not text:
        return perm
    
    if len(text) == 1:
        perm.add(text)
        return perm
    
    if len(text) == 2:
        perm.add(text[0] + text[1])
        perm.add(text[1] + text[0])
        return perm
    
    for position in range(len(text)):
        remaining_text = text[position+1:] + text[:position]
        for permutation in permutations(remaining_text):
            perm.add(text[position] + permutation)
    return perm