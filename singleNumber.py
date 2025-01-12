
def singleNumber(nums):
    for i in nums:
        nums.remove(i)
        if i in nums:
            nums.insert(0, i)
        else:
            return i
