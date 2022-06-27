class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        sum = 0 
        sum += roman_dict[s[0]]
        
        if len(s) > 1:
            for i in range(1, len(s)):
                if s[i] in ('V', 'X') and s[i-1] == 'I':
                    sum -= 2
                elif s[i] in ('L', 'C') and s[i-1] == 'X':
                    sum -= 20
                elif s[i] in ('D', 'M') and s[i-1] == 'C':
                    sum -= 200
                sum += roman_dict[s[i]]
                
        return sum
                    
   