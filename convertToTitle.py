
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        abc = [chr(i) for i in range(65, 91)]
        res = ''

        while columnNumber > 0:
            columnNumber -= 1
            res = abc[columnNumber % 26] + res
            columnNumber //= 26

        print(res)

        return res