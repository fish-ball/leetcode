class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        mm = 0
        nn = 0
        if not n:
            return 
        for i in range(m):
            nums1[-1-i] = nums1[m-1-i]
            nums1[m-i-1] = 0
        while nn < n:
            if mm >= m:
                nums1[mm+nn] = nums2[nn]
                nn += 1
            elif nums1[mm+n] <= nums2[nn]:
                nums1[mm+nn] = nums1[mm+n]
                mm += 1
            else:
                nums1[mm+nn] = nums2[nn]
                nn += 1
            # print(mm, nn, nums1, nums2[nn:n])
        # print(nums1)

    
