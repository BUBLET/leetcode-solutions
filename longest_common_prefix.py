class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:    
        res = ""
        
        short_str = min(range(len(strs)), key=lambda i: len(strs[i]))

        for j in range(len(strs[short_str])):
            try_set = set()
            for i in range(len(strs)):
                try_set.add(strs[i][j])
            if len(try_set) == 1:
                    res += strs[i][j]
            else:
                return res
                
        return res

        