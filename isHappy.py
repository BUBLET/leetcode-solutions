class Solution:
    def sumSqr(self, x: int):
            res = 0
            for i in str(x):
                res += int(i)**2
            return res

    def isHappy(self, n: int) -> bool:
        res = resF = n

        while True:
            res = self.sumSqr(res)
            resF = self.sumSqr(self.sumSqr(resF))
            if res == resF:
                break
        return res == 1