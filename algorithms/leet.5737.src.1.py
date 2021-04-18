class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        x = reduce(lambda a, b: a ^ b, arr2)
        return reduce(lambda a, b: a ^ b, [y&x for y in arr1])
