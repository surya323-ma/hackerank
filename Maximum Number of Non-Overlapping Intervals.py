Given an array of intervals where each interval has a start and end time, return the maximum number of non-overlapping intervals.

def maximizeNonOverlappingMeetings(meetings):
    meetings.sort(key=lambda x:x[1])
    count=0
    end=float('-inf')
    for start ,finish in meetings:
        if start >= end:
            count +=1
            end=finish
    return count
