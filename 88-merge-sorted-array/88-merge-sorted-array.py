class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        nums1_cp = nums1[:m]
        
        p1, p2 = 0, 0
        
        for i in range(m+n):
            if p1 >= m or (p2 < n and nums2[p2] <= nums1_cp[p1]):
                nums1[i] = nums2[p2]
                p2 += 1
            else:
                nums1[i] = nums1_cp[p1]
                p1 += 1
        