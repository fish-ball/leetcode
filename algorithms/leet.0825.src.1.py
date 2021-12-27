class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        ans = 0
        # print(ages)
        for i, x in enumerate(ages):
            j = bisect.bisect_left(ages, x//2+8)
            k = bisect.bisect_right(ages, x)
            ans += max(k - j, 0)
            if k > i and k > j:
                ans -= 1
            # print(i,j,k)
            # print(f'{x//2+8} <= y <= {x}, ans = {ans}')
        return ans
