class Solution:
    def __init__(self):
        self.mem = dict()

    def isScramble(self, s1: str, s2: str) -> bool:
        if (s1, s2) in self.mem:
            return self.mem[(s1, s2)]
        # print(f'isScramble({s1}, {s2})')
        for k in range(2):
            if s1 == s2:
                self.mem[(s1, s2)] = True
                return self.mem[(s1, s2)]
            # for i in range(len(s1)):
            #     # print(s1[i:] + s1[:i], s2)
            #     if s1[i:] + s1[:i] == s2:
            #         return True
            ctr1 = Counter()
            ctr2 = Counter()
            for i, (a, b) in enumerate(zip(s1[:-1], s2[:-1])):
                # print(i, a, b)
                ctr1 += {a: 1}
                ctr2 += {b: 1}
                if ctr1 == ctr2 and \
                        self.isScramble(s1[:i+1], s2[:i+1]) and \
                        self.isScramble(s1[i+1:], s2[i+1:]):
                    self.mem[(s1, s2)] = True
                    return self.mem[(s1, s2)]
            s1 = s1[::-1]
        self.mem[(s1, s2)] = False
        return self.mem[(s1, s2)]
        
