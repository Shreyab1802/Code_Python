class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        start_times = sorted(i[0] for i in intervals)
        end_times = sorted(i[1] for i in intervals)

        s, e = 0, 0
        rooms = 0

        while s < len(start_times):
            if start_times[s] >= end_times[e]:
                rooms -= 1
                e += 1

            rooms += 1
            s += 1

        return rooms