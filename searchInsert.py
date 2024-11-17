class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        for i in reversed(nums):
            if i < target:
                return nums.index(i) + 1
        return 0