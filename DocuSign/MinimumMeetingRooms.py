from typing import List


class Solution:
    def minMeetingRooms(intervals: List[List[int]]) -> int:

        start_times = sorted(i[0] for i in intervals)
        end_times = sorted(i[1] for i in intervals)

        s, e = 0, 0
        rooms = 0

        while s < len(start_times):
            # If thecurrentmeeting If the current meeting's ' \
            # 'start time is greater than or equal to the earliest end' \
            # ' time (i.e., start_times[s] >= end_times[e]), ' 'it means a meeting has ended, freeing up a room.' \
            # 'Therefore, decrement the room counter (rooms -= 1)
            if start_times[s] >= end_times[e]:
                rooms -= 1
                e += 1


            rooms += 1
            s += 1

        return rooms

s = Solution
intervals = [[7,10],[2,4]]
print(s.minMeetingRooms(intervals))