class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        stk = []
        for i, x in enumerate(nums2):
            while stk and nums2[stk[-1]] < x:
                d[nums2[stk[-1]]] = x
                stk.pop()
            stk.append(i)
        return [d.get(x, -1) for i, x in enumerate(nums1)]
