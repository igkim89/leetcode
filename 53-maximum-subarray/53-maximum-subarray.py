class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = -math.inf
        
        # for i in range(len(nums)):
        #     sub_sum = 0
        #     for j in range(i, len(nums)):
        #         sub_sum += nums[j]
        #         if sub_sum > result:
        #             result = sub_sum 
        
        result = prev_sum = nums[0]
        
        for i in nums[1:]:
            prev_sum = max(i, i+prev_sum)
            result = max(result, prev_sum)
    
        return result
                