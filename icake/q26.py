# Write a function to reverse a string in-place
# Python strings are immutable. So convert string
# into list of characters and join them back after
# reversing.

def reverse_text(text):
    """
    Reverse a string in place
    """
    if not text:
        raise ValueError("Text is empty or None") 
    
    start = 0
    end = len(text) - 1

    chars = list(text)

    while start <= end:
        t = chars[start]
        chars[start] = chars[end]
        chars[end] = t
        start += 1
        end -= 1
    
    return "".join(chars)