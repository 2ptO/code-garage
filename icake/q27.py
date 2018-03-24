# Write a function reverse_words() that takes a message as a list of characters
# and reverses the order of the words in-place.
# E.g. jumps fox brown quick -> quick brown fox jumps

def _reverse_word(word):
    """
    Reverse a string in place
    """
    if not word:
        raise ValueError("Text is empty or None") 
    
    start = 0
    end = len(word) - 1

    while start <= end:
        word[start], word[end] = word[end], word[start]
        start += 1
        end -= 1

def reverse_words(words):
    # reverse the full list
    # reverse every word in the list
    _reverse_word(words)
    start = 0
    end = 0
    while end <= len(words):
        if end == len(words) or words[end] == " ":
            # Found a word to reverse
            word = words[start:end]
            _reverse_word(word)
            words[start:end] = word
            start = end + 1
        end += 1
    
