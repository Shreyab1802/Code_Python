
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        remove_interval = 0
        k = -inf

        for x, y in intervals:
            if x >= k :
                k = y
            else:
                remove_interval += 1
                # start_times = [i[0] for i in intervals]
        # end_times = [i[1] for i in intervals]

        # s,e = 0, 0

        # while s < len(start_times) -1:
        # if start_times[s+1] < end_times[e]:
        # remove_interval += 1

        # e +=1
        # s += 1

        return remove_interval