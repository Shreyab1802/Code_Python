class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index = -1
        if not nums:
            return -1
        if len(nums) == 1 and nums[0] == target:
            return 0
        elif len(nums) == 1 and nums[0] != target:
            return -1
        start, end = 0, len(nums) - 1
        if nums[start] < nums[end]:
            index = 0
        else:
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] > nums[mid + 1]:
                    index = mid + 1
                    break
                else:
                    if nums[mid] < nums[start]:
                        end = mid - 1
                    else:
                        start = mid + 1

        def binsearch(l, r):
            while l <= r:
                pivot = (l + r) // 2
                if nums[pivot] == target:
                    return pivot
                elif nums[pivot] < target:
                    l = pivot + 1
                else:
                    r = pivot - 1
            return -1

        if index == 0:
            return binsearch(0, len(nums) - 1)
        elif target < nums[0]:
            return binsearch(index, len(nums) - 1)
        else:
            return binsearch(0, index)




