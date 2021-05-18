class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        acc = [0]
        for x in arr:
            acc.append(acc[-1] ^ x)
        ans = 0
        for i in range(n):
            for j in range(i):
                if acc[i+1] ^ acc[j] == 0:
                    ans  += i - j
        return ans
