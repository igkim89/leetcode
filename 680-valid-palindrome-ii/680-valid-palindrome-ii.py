class Solution:
    def validPalindrome(self, s: str) -> bool:
        while len(s) > 1:
            if s[0] == s[len(s)-1]:
                s = s[1:len(s)-1]
            else:
                valid1 = self.subValid(s[1:])
                valid2 = self.subValid(s[0:len(s)-1])
                return valid1 or valid2
        return True
                
    def subValid(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        else:
            return False