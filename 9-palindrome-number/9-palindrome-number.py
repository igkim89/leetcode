class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_list = list(map(str, str(x)))
        x_list.reverse()
        rev_x = "".join(x_list)
        
        if str(x)==rev_x:
            return True
        return False
        