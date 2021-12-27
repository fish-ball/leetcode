class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        ans = []
        for i in range(len(s)):
            x, y = startPos
            k = 0
            for j in range(i, len(s)):
                d = s[j]
                if d == 'U':
                    x-=1
                elif d == 'D':
                    x+=1
                elif d == 'L':
                    y-=1
                else:
                    y+=1
                if not(0<=x<n and 0<=y<n):
                    break
                k += 1
            ans.append(k)
        return ans
