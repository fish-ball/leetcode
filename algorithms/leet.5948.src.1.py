class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # print(f'\nquestion: {s}, {locked}', end=': ----')
        mn = 0
        mx = 0
        for x, y in zip(s, locked):
            # print('mn=%s, mx=%s' % (mn, mx))
            # print()
            # print('x=%s, y=%s' % (x, y))
            if y == '0':
                mx = mx + 1
                mn = 1 if mn==0 else mn-1
            elif x == '(':
                mn += 1
                mx += 1
            elif x == ')':
                if mx < 1:
                    return False
                mx -= 1
                if mn == 0:
                    mn = 1
                else:
                    mn -= 1
                if mn > mx:
                    return False
        
        # print('mn=%s, mx=%s' % (mn, mx))
        return mx >= mn and mx % 2 == 0 and mn == 0
                
