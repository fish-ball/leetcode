class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        last = 0
        acc = 0
        ans = 0
        for i, x in enumerate(prices):
            if x != last-1:
                print(f'acc={acc}')
                ans += acc*(acc+1)//2
                acc = 0
            acc += 1
            last = x
        # print(f'acc={acc}')
        ans += acc*(acc+1)//2
        # print(' ')
        return ans
