class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        data_set = set()
        
        for i in nums:
            data_set.add(i)
            
        return True if len(data_set) != len(nums) else False
        