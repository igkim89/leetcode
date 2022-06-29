class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        dict = {
            ")": "(", 
            "}": "{", 
            "]": "[",
        }
        
        for i in s:
            if i in dict:
                pop_char = stack.pop() if stack else False
                if pop_char != dict[i]: return False
            else:
                stack.append(i)
                
        return not stack