class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum & 1:
            return []
        ans = []
        k = 2
        while finalSum > k + k:
            ans.append(k)
            finalSum -= k
            k += 2
        ans.append(finalSum)
        return ans
