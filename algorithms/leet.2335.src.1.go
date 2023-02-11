// https://leetcode.cn/problems/minimum-amount-of-time-to-fill-cups/
// 2335. 装满杯子需要的最短总时长
func fillCups(amount []int) int {
    a, b, c := amount[0], amount[1], amount[2]
    ans := 0
    if a > b { a, b = b, a }
    if b > c { b, c = c, b }
    if a > b { a, b = b, a }
    for ; c > 0; ans++ {
        c -= 1
        if b > 0 { b -= 1 }
        if a > b { a, b = b, a }
        if b > c { b, c = c, b }
    }
    return ans
}
