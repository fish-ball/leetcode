class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        encoded.append(reduce(lambda a, b: a^b, encoded))
        neg = []
        # print(encoded)
        x = reduce(lambda a, b: a^b, encoded[1::2])
        y = reduce(lambda a, b: a^b, encoded[2::2])
        # print(x, y)
        for i in range(n):
            neg.append(x)
            # print(encoded[(i+1)%n], encoded[(n+i)%n])
            x ^= encoded[(i+1)%n]
            x ^= encoded[(n+i)%n]
            x, y = y, x
        k = reduce(lambda a, b: a^b, range(1, n+1))
        return [k ^ x for x in neg]
