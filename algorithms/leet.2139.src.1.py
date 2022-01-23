class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans = 0
        while maxDoubles and target > 1:
            if target & 1:
                ans += 2
            else:
                ans += 1
            maxDoubles -= 1    
            target >>= 1
        ans += target - 1
        return ans
        
