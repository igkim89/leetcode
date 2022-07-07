class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        digit, i, j = 0, 0, 0
        while(j<len(abbr)):
            if(abbr[j].isdigit()):
                if(abbr[j] == '0' and digit == 0):
                    return False
                digit = (digit*10)+int(abbr[j])

            else:
                i = i+digit
                digit = 0
                if(i >= len(word) or abbr[j] != word[i]):
                    return False
                i = i+1
            j = j+1

        return (len(word[i:]) == digit)