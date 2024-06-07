class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsMap = {}
        sorted_list = []
        count = 0

        for i in nums:
            if i not in numsMap:
                numsMap[i] = count + 1
            else:
                numsMap[i] = numsMap[i] + 1

        print(numsMap)
        # sorted(numsMap.items(), key=lambda kv: (kv[1], kv[0]), reverse = True)
        sorted_d = dict(sorted(numsMap.items(), key=operator.itemgetter(1), reverse=True))

        for i in sorted_d:
            if len(sorted_list) < k:
                print(i)
                sorted_list.append(i)

        print(sorted_d)

        return sorted_list

