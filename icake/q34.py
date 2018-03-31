# Write code that takes a long string and builds its word cloud data in a dictionary,
# where the keys are words and the values are the number of times the words occurred.

# Think about capitalized words. For example, look at these sentences:

#   'After beating the eggs, Dana read the next step:'
#   'Add milk and eggs, then add flour and sugar.'

# What do we want to do with "After", "Dana", and "add"
# In this example, your final dictionary should include one "Add" or "add" with a value of 2. 
# Make reasonable (not necessarily perfect) decisions about cases like "After" and "Dana".

# Assume the input will only contain words and standard punctuation.

# Assumption: treat case insensitive
# punctuations = set(standard_punctuations)
# words with hyphen, apostrophe are treated as one word
# start = 0
# end = -1
# word_cloud = collections.defaultdict()
# for word in get_words(sentence):
#    word_cloud[word] += 1
# get_words(sentence, start, end)
#   
#   find first non-punctuation from start between length(sentence)
#   from first non-punctuation, find the next punctuation mark until length(sentence)
#   return sentence[start:end]

import collections

# TODO This version has some flaws. The last char in the given text
# has to be a punctuation for this version to work
def get_words(text):
    index = 0
    first_alpha_pos = 0
    first_non_alpha = -1

    # Walk through the text to find each word
    while index < len(text):
        first_alpha_pos = index
        index = first_non_alpha + 1
        while (index < len(text)):
            # Treat hyphens and apostrophe's as part of a word
            if text[index].isalpha() or text[index] == '\'' or text[index] == '-':
                first_alpha_pos = index
                break
            index += 1
    
        index = first_alpha_pos + 1
        while (index < len(text)):
            if not (text[index].isalpha() or text[index] == '\'' or text[index] == '-'):
                first_non_alpha = index
                yield text[first_alpha_pos:first_non_alpha]
                # Found a word.
                break
            index += 1

def get_word_cloud(text):
    word_cloud = collections.defaultdict(int)
    for word in get_words(text):
        # for simplicity reasons, converting everything to lower case.
        # The tradeoff is that we lose meaning from the words of the
        # given text. E.g. Proper noun "Ken" is different from noun "ken".
        word_cloud[word.lower()] += 1
    
    return word_cloud

# sample texts
text = "We came, we saw, we conquered...then we ate Bill's (Mille-Feuille) cake."
print(text)
for key, value in get_word_cloud(text).items():
    print(key, value)

text = "After beating the eggs, Dana read the next step:"
text += " Add milk and eggs, then add flour and sugar."
print(text)
for key, value in get_word_cloud(text).items():
    print(key, value)

# Approached the problem with right breakdown of sub problems
# Need to look deeper in considering different solutions and
# trade off for each of them. will get back to split words
# later 