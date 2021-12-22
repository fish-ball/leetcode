class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i, a in enumerate(numbers):
            j = bisect.bisect_left(numbers, target-a, i+1, n)
            if 0 <= j < n and a+numbers[j]==target:
                return [i+1, j+1]
