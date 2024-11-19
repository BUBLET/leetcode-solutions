class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = "0b" + a
        b = "0b" + b
        res = bin(int(a, 2) + int(b, 2))
        return res[2:]


solution = Solution()
a = "11"
b = "1"
x = solution.addBinary(a, b)
print(x)