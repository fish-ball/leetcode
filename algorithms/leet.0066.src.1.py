class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        carry = 1
        for i, x in enumerate(digits):
            digits[i] += carry
            if digits[i] < 10:
                carry = 0
                break
            digits[i] = 0
        if carry:
            digits.append(1)
        return digits[::-1]
