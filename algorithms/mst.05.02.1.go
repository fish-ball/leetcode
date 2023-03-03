// https://leetcode.cn/problems/bianry-number-to-string-lcci/
// 面试题 05.02. 二进制数转字符串

func printBin(num float64) string {
    ans := "0."
    d := float64(0.5)
    eps := float64(1e-10)
    for i:=0; i<6; i++ {
        if num + eps > d {
            ans += "1"
            num -= d
        } else {
            ans += "0"
        }
        d *= .5
        if num < eps {
            return ans
        }
    }
    return "ERROR"
}
