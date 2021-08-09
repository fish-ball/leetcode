class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        q = primes[:]
        heapq.heapify(q)
        pp = 1
        for k in range(n-1):
            while q[0] == pp:
                heapq.heappop(q)
            pp = heapq.heappop(q)
            # print(pp)
            for x in primes:
                heapq.heappush(q, pp*x)
        return pp
