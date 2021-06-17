class Solution:
    def isNumber(self, s: str) -> bool:
        return bool(re.match(f'[+-]?(?:\d*\.?\d+|\d+\.\d*)(?:[eE][+-]?\d+)?$', s))
