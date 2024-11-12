class Solution: 
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")": "(", "]": "[", "}": "{"}
        for char in s:  
            if char in "({[":
                stack.insert(0, char)
            elif char in "]})":
                if not stack or stack[0] != pairs[char]:
                    return False
                stack.pop(0)
        
        return len(stack) == 0