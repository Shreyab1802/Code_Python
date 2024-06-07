class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #
        # n = len(temperatures)
        #answer = [0]*n

        #for i in range(n):
         #    for future_day in range(i + 1, n):
           #      if temperatures[future_day] > temperatures[i]:
             #        answer[i] = future_day - i
               #      break
         #return answer

# We will use Monotonic stacks which will keep on adding the temperatures along with
# it's index as long as the next temperature in list is greater than that and as soon
# as a warmer temperature is found we will pop the item from top of the stack

        result = [0] * len(temperatures)
        stack = [] # par:[temperature,index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackI = stack.pop()
                result[stackI] = (i - stackI)
            stack.append(t,i)
        return result
