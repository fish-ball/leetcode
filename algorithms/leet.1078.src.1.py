class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        idx = 0
        ans = []
        text = ' ' + text + ' '
        ll = len(f' {first} {second} ')
        while True:
            idx = text.find(f' {first} {second} ', idx)
            if idx == -1:
                break
            idx2 = text.find(' ', idx+ll)
            # print(idx, idx2, text[idx:idx2])
            if idx+ll < idx2:
                ans.append(text[idx+ll:idx2])
            idx = text.find(' ', idx+1)
        return ans
