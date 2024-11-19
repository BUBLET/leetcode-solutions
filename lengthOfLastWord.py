class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if " " not in s:
            return len(s)
        count = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] != " ":
                count += 1
            elif count == 0:
                continue
            else:
                return count
        return count
    
