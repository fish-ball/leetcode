// https://leetcode.cn/problems/circular-permutation-in-binary-representation/
// 1238. 循环码排列 - 格雷码生成，按照贪心搜索必然找到回路

func circularPermutation(n int, start int) []int {
    m := 1<<n
    b := make([]bool, m)
    ans := []int{}
    for i:=0; i<m; i++ {
        b[start] = true
        ans = append(ans, start)
        for j:=1; j<m; j<<=1 {
            if !b[start^j] {
                start ^= j
                break
            }
        }
    }
    return ans
}
