from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        setr = set(nums)
        for i in setr:
            if nums.count(i) > len(nums) / 2:
                return i
                