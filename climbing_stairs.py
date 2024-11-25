class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0, 1, 2]
        for i in range(3, 46, 1):
            count = dp[i-1] + dp[i-2]
            dp.append(count)
        return dp[n]
                