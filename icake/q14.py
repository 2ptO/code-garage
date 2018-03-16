# Users on longer flights like to start a second movie right when their 
# first one ends, but they complain that the plane usually lands before
# they can see the ending. So you're building a feature for choosing two
# movies whose total runtimes will equal the exact flight length.

# Write a function that takes an integer flight_length (in minutes) and 
# a list of integers movie_lengths (in minutes) and returns a boolean
# indicating whether there are two numbers in movie_lengths whose sum
# equals flight_length.

# When building your function:

# Assume your users will watch exactly two movies
# Don't make your users watch the same movie twice
# Optimize for runtime over memory

def is_movie_time_matching_flight_time(flight_time, movie_lengths):
    
    # Note: If we try to directly convert the movie_lengths list into
    # a set, we would lose duplicates in that. So if we two different
    # movies have the same length, then we will return a wrong answer
    # in that case. So don't try to convert the movie_lengths into
    # set early on

    second_movie_lengths = set()
    for first_movie_length in movie_lengths:
        second_movie_length = flight_time - first_movie_length
        # it is possible for the first_movie_length to be greater
        # than the flight time too. In which case, second_movie_length
        # would be negative. If we have accidentally have another negative
        # length in given movie lengths, then we will return a
        # false positive. So lets make sure that there are no negative
        # movie lengths.
        if first_movie_length < 0:
            raise ValueError("Movie length can't be negative")

        if second_movie_length in second_movie_lengths:
            return True
        else:
            second_movie_lengths.add(first_movie_length)

    # All timings exhausted.
    return False

# I solved it for O(n2) first, then tried to optimize it further. 
# If the movie lenghts was pre-sorted, we could have used binary
# search to search for the second movie length and solved this
# in O(nlog(n)) time without the additional O(n) space required
# to store the second movie lengths
