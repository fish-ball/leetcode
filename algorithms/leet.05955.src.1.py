class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        s = 0
        acc = [0]
        for i, (x, a) in enumerate(fruits):
            s += a
            acc.append(s)
        ans = 0
        for i, (x, a) in enumerate(fruits):
            if x < startPos:
                y = max(k+x+x-startPos, (k+x+startPos)//2)
                if y < startPos:
                    continue
            else:
                y = startPos + k
            j = bisect.bisect_right(fruits, [y, 99999])
            # print(x, startPos, y, fruits[j-1], fruits[i], acc[j] - acc[i])
            ans = max(ans, acc[j] - acc[i])
        # print('')
        return ans
      
