class Solution:
    def isValid(self, s: str) -> bool:

        map_dict = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            if char not in map_dict:
                stack.append(char)


            else:
                if not stack or stack[-1] != map_dict[char]:
                    return False
                stack.pop()
        return not stack