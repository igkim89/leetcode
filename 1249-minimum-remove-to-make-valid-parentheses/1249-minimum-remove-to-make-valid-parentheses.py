class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_stack = []
        remove_set = set()
        result = ""
        
        for i, c in enumerate(s):
            if c == "(":
                open_stack.append(i)
            elif c == ")":
                if open_stack:
                    open_stack.pop()
                else:
                    remove_set.add(i)
        
        remove_set = remove_set.union(set(open_stack))
             
        for i, c in enumerate(s):
            if i not in remove_set:
                result += c
            
        return result
