class Solution:
    def maximumTime(self, time: str) -> str:
        tt = list(time)
        if tt[0] == '?':
            if tt[1] in '0123?':
                tt[0] = '2'
            else:
                tt[0] = '1'
        if tt[1] == '?':
            if tt[0] == '2':
                tt[1] = '3'
            else:
                tt[1] = '9'
        if tt[3] == '?':
            tt[3] = '5'
        if tt[4] == '?':
            tt[4] = '9'
        return ''.join(tt)
