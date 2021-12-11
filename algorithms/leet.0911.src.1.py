class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        rank = []
        idx = {}
        self.log = [[-1, -1]]
        for k, t in zip(persons, times):
            # print(k, t)
            if k not in idx:
                rank.append([k, 0])
                idx[k] = len(rank) - 1
            i = idx[k]
            rank[i][1] += 1
            while i > 0 and rank[i][1] >= rank[i-1][1]:
                rank[i], rank[i-1] = rank[i-1], rank[i]
                idx[rank[i][0]] = i
                idx[rank[i-1][0]] = i-1
                i -= 1
            # print(rank)
            winner = rank[0][0]
            if self.log[-1][1] != winner:
                self.log.append([t, winner])
        # print(self.log)

    def q(self, t: int) -> int:
        x = bisect.bisect_right(self.log, [t+1, -1])
        # print(t, x)
        # print(self.log[x-1])
        return self.log[x-1][1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
