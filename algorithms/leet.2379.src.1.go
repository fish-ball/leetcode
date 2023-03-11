// https://leetcode.cn/problems/minimum-recolors-to-get-k-consecutive-black-blocks/
// 2379. 得到 K 个黑块的最少涂色次数

func minimumRecolors(blocks string, k int) int {
    acc := 0
    for i:=0; i<k; i++ {
        if blocks[i] == 'W' { acc++ }
    }
    ans := acc
    for i:=k; i<len(blocks); i++ {
        if blocks[i] == 'W' { acc++ }
        if blocks[i-k] == 'W' { acc-- }
        if ans > acc { ans = acc }
    }
    return ans
}
