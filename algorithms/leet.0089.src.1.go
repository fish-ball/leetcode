// https://leetcode.cn/problems/gray-code/
// 89. 格雷编码 - 神奇的构造法

func grayCode(n int) []int {
    ans := []int{}
    for i,x:=0,0; i<(1<<n); i++ {
        ans = append(ans, x)
        x ^= ^i&(i+1)
    }
    return ans
}
