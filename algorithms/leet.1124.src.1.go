// https://leetcode.cn/problems/longest-well-performing-interval/
// 1124. 表现良好的最长时间段
// 生成一个累加数组 acc，逢>8就+1，否则-1
// 维护一个字典，mp[x]=j 表示出现累加值比特定的 x 小的最早位置是 j
// 然后每到某个 i 的位置，求 i - mp[acc[i]-1] 的最大值就可以了

func longestWPI(hours []int) int {
    n := len(hours)
    acc := make([]int, n)
    ans := 0
    // 记录小于特定的值最早出现的时间
    mp := map[int]int{}
    mp[0] = -1
    last := 0
    for i, x := range hours {
        if x > 8 {
            last++
            if _, ok := mp[last]; !ok {
                mp[last] = mp[last-1]
            }
        } else {
            last--
            if _, ok := mp[last]; !ok {
                mp[last] = i
            }
        }
        acc[i] = last
        if j, ok := mp[last-1]; ok && i - j > ans { 
            ans = i - j
        }
    }
    return ans
}
