def isAnagram(self, s: str, t: str) -> int:
    if (len(s) != len(t)):
        return False

    map_s = {}
    map_t = {}

    for i in s:
        # print(i)
        if (i in map_s):
            map_s[i] += 1
        else:
            map_s[i] = 1

    for j in t:
        # print(i)
        if (j in map_t):
            map_t[j] += 1
        else:
            map_t[j] = 1

    # print(map_s)
    # print(map_t)

    for item in map_s:
        # print(item)
        if map_s[item] != map_t.get(item, 0):
            return False

    return True