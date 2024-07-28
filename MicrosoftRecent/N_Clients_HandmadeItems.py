# There are N clients who have ordered N handmade items. The K-th client ordered exactly one
# item that takes T[K] hours to make. There is only one employee who makes items for clients,
# and he/she works in the following manner:
# spend 1 hour making the first item
# if the item is finished, deliver it
# if the item is NOT finished, put it after ALL REMAINING ITEMS for futher work
# employee then works on next item
# What is the total time that clients need to wait for all ordered items?


def solve(nums):

  time_taken = 0
  n = len(nums)
  smaller_nums = [float('inf')]
  smaller_nums2 = [float('inf')]
  for i in range(n):
    smaller_nums.append(
      min(nums[i] - 1, smaller_nums[-1])
    )
  for i in range(n-1, -1, -1):
    smaller_nums2.append(
      min(nums[i] - 1, smaller_nums2[-1])
    )

  for i in range(n):
    time = nums[i] - 1
    for j in range(i):
      time += min(nums[j] - 1, nums[i] - 1)
    for j in range(i+1, n):
      time += min(nums[i]-1, nums[j])
    time_taken += (i + time + 1)
  return time_taken % (10**9)

# Test cases
print(solve([3, 1, 2]))  # Output: 13
print(solve([1, 2, 3, 4]))  # Output: 24
print(solve([7, 7, 7]))  # Output: 60
print(solve([10000]))  # Output: 10000



#### solution 2

from collections import deque


def solve(T):
    n = len(T)
    queue = deque(range(n))
    remaining_time = T[:]
    current_time = 0
    total_wait_time = 0

    while queue:
        client = queue.popleft()
        current_time += 1
        remaining_time[client] -= 1
        if remaining_time[client] == 0:
            total_wait_time += current_time
        else:
            queue.append(client)

    return total_wait_time


# Test cases
print(solve([3, 1, 2]))  # Output: 13
print(solve([1, 2, 3, 4]))  # Output: 24
print(solve([7, 7, 7]))  # Output: 60
print(solve([10000]))  # Output: 10000
