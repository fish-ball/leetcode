class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n = len(pushed)
        a = []
        i = 0
        for x in popped:
            while a and a[-1] != x or not a:
                if i == n:
                    return False
                a.append(pushed[i])
                i += 1
            a.pop()
        return True
