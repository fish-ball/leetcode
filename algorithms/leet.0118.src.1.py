class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(numRows-1):
            ans.append([0] + ans[-1])
            for j in range(i+1):
                ans[-1][j] += ans[-1][j+1]
        return ans
