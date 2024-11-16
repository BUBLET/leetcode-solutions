class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        myset = set()
        newnums = []
        for i in nums:
            if i not in myset:
                myset.add(i)
        for i in sorted(myset):
            newnums.append(i)
        nums.clear()       # Удаляем все элементы из nums
        nums.extend(newnums)
        return len(newnums)
