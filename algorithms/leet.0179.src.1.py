# from functools import cmp_to_key
# sorted(mylist, key=cmp_to_key(compare))    

class Solution:

    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            # print(f'compare: {x}, {y}')
            for xx, yy in zip(x, y):
                if xx < yy:
                    return 1
                elif xx > yy:
                    return -1
            if len(x) < len(y):
                return compare(x, y[len(x):])
            elif len(x) > len(y):
                return compare(x[len(y):], y)
            return 0

        ans = ''.join(sorted(map(str, nums), key=cmp_to_key(compare)))
        return '0' if ans.startswith('0') else ans
