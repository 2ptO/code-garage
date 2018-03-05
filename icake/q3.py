# Your company built an in-house calendar tool called HiCal. You want to add
# a feature to see the times in a day when everyone is available.

# To do this, you’ll need to know when any team is having a meeting. In HiCal,
# a meeting is stored as a tuple ↴ of integers (start_time, end_time).
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

print(merge_ranges([(0, 1), (3, 5), (4, 8), (9, 12), (2, 4)]))