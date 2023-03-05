// https://leetcode.cn/problems/maximum-profit-of-operating-a-centennial-wheel/
// 1599. 经营摩天轮的最大利润

func minOperationsMaxProfit(customers []int, boardingCost int, runningCost int) int {
    mx := -1
    n := 0
    k := 1
    rem := 0
    ans := -1
    for _, x := range customers {
        rem += x
        if rem >= 4 {
            n += 4
            rem -= 4
        } else {
            n += rem
            rem = 0
        }
        acc := boardingCost * n - runningCost * (k + 1) 
        if acc > mx {
            mx = acc
            ans = k
        }
        k++
    }
    for rem > 0 {
        if rem >= 4 {
            n += 4
            rem -= 4
        } else {
            n += rem
            rem = 0
        }
        acc := boardingCost * n - runningCost * (k + 1)
        if acc > mx {
            mx = acc
            ans = k
        }
        k++
    }
    return ans
}
