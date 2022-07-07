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

    #오늘의 가르침
    #중복이 없는 경우 set을 쓰자 짱짱 빠르다