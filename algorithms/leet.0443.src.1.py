class Solution:
    def compress(self, chars: List[str]) -> int:
        last = ''
        k = 0
        m = 0
        def enqueue(x):
            nonlocal m
            chars[m] = last
            m += 1
            if k > 1:
                for d in str(k):
                    chars[m] = d
                    m += 1

        for c in chars:
            if c != last:
                if last:
                    enqueue(last)
                last = c
                k = 1
            else:
                k += 1
        enqueue(last)
        del chars[m:]
        return m

