class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num < 2:
            return False
        acc = 1
        k = 2
        while k < num and k * k < num:
            if num % k == 0:
                acc += k + num / k
            k += 1
        if k * k == num:
            acc += k
        return num == acc
