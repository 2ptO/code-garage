# write a function to tell us if a full deck of cards 
# shuffled_deck is a single riffle of two other halves
# half1 and half2.

# We'll represent a stack of cards as a list of integers
# in the range 1..52(since there are 52 distinct cards in a deck).

def is_riffle(shuffled_deck):
    half1 = set(list(range(1, 27)))
    half2 = set(list(range(27, 53)))

    if len(shuffled_deck) != 52:
        raise ValueError("Insufficient cards in the deck")

    first_deck = half1 if shuffled_deck[0] in half1 else half2
    second_deck = half2 if first_deck == half1 else half1

    for index, card in enumerate(shuffled_deck):
        if index % 2 == 0 and card not in first_deck:
            return False
        if index % 2 == 1 and card not in second_deck:
            return False
    
    return True
            
        