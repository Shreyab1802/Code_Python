class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}

        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s not in map:
                map[sorted_s] = []
            map[sorted_s].append(s)
        return map.values()