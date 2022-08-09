class Solution:
    #     def isValid(self, s: str) -> bool:
    #         map = { "(" : ")", "}": "{", "]" : "["}
    #         stack = [ ]

    #         for i in s:
    #             if i in map:
    #                 #if this is closing parenthesis
    #                 # stack is not empty and top value of stack is closing char parenthesis
    #                 if stack and stack[-1] == map[i]:
    #                     stack.pop()
    #                     print(stack.pop())

    #                 else:
    #                     # don't match and stack is empty
    #                     return False
    #             else:
    #                 # if we get an open parenthesis, keep going append it
    #                 stack.append(i)

    #         return True if not stack else False

    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s: #iterating through input
            if c not in Map:# for opeining parathesis we will keep on appending
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]: #stack is empty and top of stack not matches with the value of opening parathesis
                return False
            stack.pop()

        return not stack
