class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        list3 = nums1 + nums2

        print(list3)

        list3 = sorted(list3)

        print(list3)

        n = len(list3)

        if n == 2:
            return (list3[0] + list3[1]) / 2
        else:
            if (n % 2 == 0):
                return (list3[int(n / 2)] + list3[int(n / 2) - 1]) / 2
            else:
                middle = int((n - 1) / 2)
                return list3[middle]
