class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        tmp = ""
        result = ""
        min_len = min(iter(len(i) for i in strs))
        
        if len(strs) == 1:
            result = strs[0]
        else:
            for i in range(min_len):
                
                tmp = strs[0][i]
                
                for j in range(1, len(strs)):
                    if tmp != strs[j][i]:
                        tmp = ""
                
                if tmp != "":
                    result += tmp
                else:
                    break
                    
        return result