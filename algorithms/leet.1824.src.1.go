// https://leetcode.cn/problems/minimum-sideway-jumps/
// 1824. 最少侧跳次数 - 贪心算法
func minSideJumps(obstacles []int) int {
    n := len(obstacles)
    a := [3]int{n, 0, n}
    for _, x := range obstacles {
        a0, a1, a2 := a[0], a[1], a[2]
        switch x {
        case 0:
            if a0 > a[1] + 1 { a0 = a[1] + 1 }
            if a0 > a[2] + 1 { a0 = a[2] + 1 }
            if a1 > a[0] + 1 { a1 = a[0] + 1 }
            if a1 > a[2] + 1 { a1 = a[2] + 1 }
            if a2 > a[0] + 1 { a2 = a[0] + 1 }
            if a2 > a[1] + 1 { a2 = a[1] + 1 }
        case 1:
            a0 = n
            if a1 > a[2] + 1 { a1 = a[2] + 1 }
            if a2 > a[1] + 1 { a2 = a[1] + 1 }
        case 2:
            a1 = n
            if a0 > a[2] + 1 { a0 = a[2] + 1 }
            if a2 > a[0] + 1 { a2 = a[0] + 1 }
        case 3:
            a2 = n
            if a0 > a[1] + 1 { a0 = a[1] + 1 }
            if a1 > a[0] + 1 { a1 = a[0] + 1 }
        }
        a[0], a[1], a[2] = a0, a1, a2
        // fmt.Println(x, a)
    }
    y := a[0]
    if a[1] < y { y = a[1] }
    if a[2] < y { y = a[2] }
    return y
}
