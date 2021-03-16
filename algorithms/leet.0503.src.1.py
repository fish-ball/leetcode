import heapq

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = [-1] * n
        hp = list()

        for i in range(n * 2 - 1):
            # print('heap', hp)
            ii = i % n
            while hp and hp[0][0] < nums[ii]:
                v, k = heapq.heappop(hp)
                # print(f'pop: {v}, {k}')
                ret[k] = nums[ii]
                # print(ret)
            if i < n:
                heapq.heappush(hp, (nums[ii], ii))
                # print(f'push: {nums[ii]}, {ii}')
        return ret
