class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        n = 0
        if num1 > num2:
            num1, num2 = num2, num1
        while num1:
            n += num2 // num1
            num2, num1 = num1, num2%num1
        return n
