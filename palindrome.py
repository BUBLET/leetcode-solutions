class Solution:
    def isPalindrome(self, x: int) -> bool:
        d = 1
        res = 0
        y = x
        if x < 0:
            return False
        while x > 0:
            d = x % 10
            x = (x-d)/10
            res = res*10 + d
        print(res, y)
        if res == y:
            return True
        else:
            return False