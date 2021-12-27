class Solution:
    def abbreviateProduct(self, left: int, right: int) -> str:
        
        tens = 0
        
        suffix = 1
        for x in range(left, right+1):
            suffix *= x
            while suffix % 10 == 0:
                suffix //= 10
                tens += 1
            suffix = suffix % 1000000000
        suffix = suffix % 100000
            
        bk = False
        prefix = 1
        # fpre = 1.0
        for x in range(left, right+1):
            # fpre *= x
            # fpre /= 10**(int(math.log(fpre)/math.log(10)))
            while x % 10 == 0:
                x //= 10
            prefix *= x
            while prefix % 10 == 0:
                prefix //= 10
            while prefix >= 100000000000000000:
                bk = True
                prefix //= 10
        # print(fpre)
        
            
        if not bk and len(str(prefix))<=10:
            return f'{prefix}e{tens}'
        
        prefix = str(prefix)[:5]
        # return f'{fpre*10000:0.0f}...{suffix:05d}e{tens}'
        return f'{prefix}...{suffix:05d}e{tens}'
        
