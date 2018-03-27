# Write a function that takes:

# a list of unsorted_scores
# the highest_possible_score in the game
# and returns a sorted list of scores in less than O(n*log(n)) time.

# For example:

#   unsorted_scores = [37, 89, 41, 65, 91, 53]
# HIGHEST_POSSIBLE_SCORE = 100

# sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE)
# # returns [91, 89, 65, 53, 41, 37]

def sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE=100):
    score_board = [0] * (HIGHEST_POSSIBLE_SCORE+1)
    for score in unsorted_scores:
        score_board[score] += 1

    sorted_scores = []
    for score in range(HIGHEST_POSSIBLE_SCORE, -1, -1):
        for _ in range(score_board[score]):
            sorted_scores.append(score)
    
    return sorted_scores

# This is an example of counting sort. Optimizing for better
# time by trading a little in space cost. O(n) time, and
# O(n) space. 