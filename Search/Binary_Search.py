nums = [2,3,3,3,7]
output = []

def binary_search(nums, start, end,target):
    if end >= start:
        mid = (start+end)//2

        if nums[mid] == target:
            return output.append(mid)
        elif nums[mid] > target:
            return binary_search(nums, start, mid - 1, target)
        else:
            return binary_search(nums, mid + 1, end, target)


    else:
        return -1

binary_search(nums, 0, len(nums)-1, 3)
print(output)