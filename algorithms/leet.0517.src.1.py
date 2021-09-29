class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        n = len(machines)
        s = sum(machines)
        if s % n != 0:
            return -1
        s //= n
        c = [0] * n
        d = [0] * n
        for i in range(n-1):
            carry = s - machines[i]
            if carry < 0:
                c[i] += -carry
            else:
                d[i+1] += carry
            machines[i+1] -= carry
            machines[i] += carry
            # print(machines)
        return max([c[i] + d[i] for i in range(n)])
