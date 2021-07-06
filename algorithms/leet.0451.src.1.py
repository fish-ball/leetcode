class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join([k * v for v, k in sorted([(v, k) for k, v in Counter(s).items()], reverse=True)])
