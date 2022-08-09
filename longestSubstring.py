# print("Hello Shreya")
# list = [1,2,3,4,5]
# print(list[])

class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        # increase the start only when u found repeating character
        max_length = start = 0
        dict = {}

        for i in range(len(s)):
            if s[i] in dict and start <= map[s[i]]:
                start = map[s[i]] + 1
            else:
                max_length = max(max_length, i - start + 1)

            dict[s[i]] = i

        return max_length

    # 2 solution
    class Solution:
        def lengthOfLongestSubstring(self, s: str) -> int:
            str_list = []
            max_length = 0

            for x in s:
                if x in str_list:
                    str_list = str_list[str_list.index(x) + 1:]

                str_list.append(x)
                max_length = max(max_length, len(str_list))

            return max_length