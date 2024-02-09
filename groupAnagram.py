from typing import List


def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    map = {}

    for s in strs:
        sorted_strs = "".join(sorted(s))
        # print(sorted_strs)
        if sorted_strs not in map:
            map[sorted_strs] = []

        map[sorted_strs].append(s)
        # print(map[sorted_strs])

    return map.values()


# Your input
# ["eat","tea","tan","ate","nat","bat"]
# Output
# [["eat","tea","ate"],["tan","nat"],["bat"]]
# Expected
# [["bat"],["nat","tan"],["ate","eat","tea"]]