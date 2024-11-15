class Solution:
    def isPalindrome(self, x: int) -> bool:
        res = 0
        y = x
        if x < 0:
            return False
        while x > 0:
            res = res*10 + x % 10
            x = (x - x % 10)/10 
        if res == y:
            return True
        else:
            return False