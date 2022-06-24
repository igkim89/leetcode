class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i_len = len(nums)-1
        j_len = len(nums)
        for i in range(i_len):
            for j in range(1, j_len):
                if nums[i] + nums[i+j] == target:
                    return [i, i+j]
            j_len -= 1