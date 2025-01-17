class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        abc = [chr(i) for i in range(65, 91)]
        res = 0
        i = 0
        lngt = len(columnTitle) - 1

        while lngt > -1:
            res += (abc.index(columnTitle[i]) + 1) * 26**lngt
            i += 1
            lngt -= 1

        return res