class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_stack = []
        close_stack = []
        remove_index = []
        result = ""
        
        for i, c in enumerate(s):
            if c == "(":
                open_stack.append(i)
            elif c == ")":
                if open_stack:
                    open_stack.pop()
                else:
                    close_stack.append(i)
        
        remove_list = open_stack + close_stack
             
        for i, c in enumerate(s):
            if i not in remove_list:
                result += c
            
        return result
                    