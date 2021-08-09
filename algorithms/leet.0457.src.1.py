class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        def nxt(i):
            return (i + n + nums[i]) % n
        for i in range(n):
            # print(nums)
            if nums[i] % n == 0:
                nums[i] = 0
                continue
            p = q = i
            while True:
                p = nxt(p)
                q = nxt(q)
                if nums[q] * nums[i] < 0:
                    break
                q = nxt(q)
                if nums[q] * nums[i] < 0:
                    break
                if nums[p] % n == 0:
                    break
                if q == p:
                    return True
            p = i
            while q != p:
                k = p
                p = nxt(p)
                nums[k] = 0
        return False
