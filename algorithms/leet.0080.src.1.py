class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last = None
        stage = 0
        m = 0
        for x in nums:
            if x == last:
                if stage == 2:
                    continue
                stage += 1
            else:
                stage = 1
            last = x
            nums[m] = x
            m += 1
        return m
