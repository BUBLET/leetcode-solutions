from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        res = []
        i, j = 0, 0
        nums1[:] = nums1[:m]
        nums2[:] = nums2[:n]
        nums1_c = nums1.copy()
        nums2_c = nums2.copy()
        
        while nums1_c and nums2_c:
            while i < len(nums1) and j < len(nums2):
                if nums1[i] <= nums2[j]:
                    res.append(nums1[i])
                    i += 1
                    nums1_c.remove(nums1[i-1])
                else:
                    res.append(nums2[j])
                    j += 1
                    nums2_c.remove(nums2[j-1])

        if nums1_c:
            res += nums1_c
        else:
            res += nums2_c

        nums1.clear()
        nums1.extend(res)
