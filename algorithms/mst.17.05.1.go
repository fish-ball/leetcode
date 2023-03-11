// https://leetcode.cn/problems/find-longest-subarray-lcci/submissions/
// 面试题 17.05.  字母与数字

func findLongestSubarray(array []string) []string {
    acc := 0
    mp := map[int]int{0:0}
    i1, j1 := 0, 0
    for i, x := range array {
        if x[0]>='0' && x[0]<='9' { acc++ } else { acc-- }
        if j, ok := mp[acc]; ok {
            if i+1-j > i1-j1 { i1, j1 = i+1, j }
        } else {
            mp[acc] = i+1
        }
        
    }
    return array[j1:i1]
}
