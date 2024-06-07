class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        bloomStartTime = sorted([s for s, e in flowers])
        bloomEndTime = sorted([e for s, e in flowers])

        return [bisect_right(bloomStartTime, arrivalTime) - bisect_left(bloomEndTime, arrivalTime) for arrivalTime in
                people]