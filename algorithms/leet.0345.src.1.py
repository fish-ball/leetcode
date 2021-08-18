class Solution:
    def reverseVowels(self, s: str) -> str:
        stk = [c for c in s if c in 'aeiouAEIOU']
        return ''.join(stk.pop() if c in 'aeiouAEIOU' else c for c in s)
