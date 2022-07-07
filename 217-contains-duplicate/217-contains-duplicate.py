class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return True if len(nums) != len(set(nums)) else False
        
#         data_set = set()
        
#         for i in nums:
#             data_set.add(i)
            
#         return True if len(data_set) != len(nums) else False
        
#         data_list = []
        
#         for i in nums:
#             if i in data_list:
#                 return True
#             else:
#                 data_list.append(i)
        
#         return False