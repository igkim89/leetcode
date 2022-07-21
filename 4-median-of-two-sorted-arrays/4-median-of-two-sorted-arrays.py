class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_list = nums1 + nums2
        merged_list.sort()
        
        if len(merged_list) == 1:
            return float(merged_list[0])
        elif len(merged_list) % 2 == 0:
            m_len = int(len(merged_list)/2)
            return float((merged_list[m_len-1] + merged_list[m_len])/2)
        else:
            m_len = len(merged_list)//2
            return float(merged_list[m_len])