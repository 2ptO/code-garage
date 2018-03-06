# Your company built an in-house calendar tool called HiCal. You want to add
# a feature to see the times in a day when everyone is available.

# To do this, you will need to know when any team is having a meeting. In HiCal,
# a meeting is stored as a tuple of integers (start_time, end_time).
# These integers represent the number of 30-minute blocks past 9:00am.

# Write a function merge_ranges() that takes a list of multiple meeting time ranges and returns a list of condensed ranges.

# For example, given:

#   [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

# your function would return:

#   [(0, 1), (3, 8), (9, 12)]

def merge_ranges(meeting_times):
    merged_times = []
    for start1, end1 in meeting_times:
        for start2, end2 in meeting_times:
            if end1 >= start2 and start1 <= end2: # we have a overlap
                start1 = min(start1, start2)
                end1 = max(end1, end2)
            
        if (start1, end1) not in merged_times:
            merged_times.append((start1, end1))

    return merged_times

def merge_ranges_optimized(meeting_times):
    """ The function is same as merge_ranges but runs in O(nlog(n)) time """
    if len(meeting_times) < 1:
        return meeting_times

    sorted_times = sorted(meeting_times)
    merged_times = [sorted_times[0]]
    for current_start, current_end in sorted_times[1:]:
        previous_start, previous_end = merged_times[-1]
        if previous_end >= current_start: # we have a overlap
            merged_times[-1] = (previous_start, max(previous_end, current_end))
        else:
            merged_times.append((current_start, current_end))

    return merged_times

# My takeaway:
# I took some time initially, and then worked out few examples
# and solved it in O(n2) time. I tried to optimize for O(n) for
# a while. I realized that O(n) is not possible when I looked
# for a hint. Then used sorting to solve this in O(nlog(n))