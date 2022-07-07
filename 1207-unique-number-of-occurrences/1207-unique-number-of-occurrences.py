class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        data_dict = {}
        data_set = set()
        
        for i in arr:
            data_dict[i] = data_dict.get(i, 1) + 1
        
        for i in data_dict.values():
            data_set.add(i)
            
        return True if len(data_dict) == len(data_set) else False