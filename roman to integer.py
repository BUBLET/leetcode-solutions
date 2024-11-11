class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        lenS = len(s) - 1
        roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        for i in range(lenS, -1, -1):
                res += roman.get(s[i])
                if i+1 < lenS:
                    if roman.get(s[i]) < roman.get(s[i+1]):
                        res -= roman.get(s[i])*2
        if roman.get(s[lenS]) > roman.get(s[lenS-1]):
            res -= roman.get(s[lenS-1])*2
        return res