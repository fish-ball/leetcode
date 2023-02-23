// https://leetcode.cn/problems/circular-permutation-in-binary-representation/
// 1238. 循环码排列 - 格雷码生成，找到规律后，按照每次翻转位为 i&(i-1) 可以直接构造出来

func circularPermutation(n int, start int) []int {
    m := 1<<n
    ans := []int{}
    for i:=1; i<=m; i++ {
        ans = append(ans, start)
        start ^= i&^(i-1)
    }
    return ans
}
