class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        r0 = len(nums)
        c0 = len(nums[0])
        if r0 * c0 != r * c:
            return nums
        return [[nums[(rr*c+cc)//c0][(rr*c+cc)%c0] for cc in range(c)] for rr in range(r)]
