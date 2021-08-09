class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        ans = [label]
        for i in range(20, 0, -1):
            if label <= (1<<i) - 1:
                continue
            label = ((1<<i)*3-label-1) // 2
            ans.append(label)
        return ans[::-1]
