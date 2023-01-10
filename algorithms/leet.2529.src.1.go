// https://leetcode.cn/problems/maximum-count-of-positive-integer-and-negative-integer/
// 2529. 正整数和负整数的最大计数

func maximumCount(nums []int) int {
    a, b := 0, 0
    for _, x := range nums {
        if x > 0 { a++ }
        if x < 0 { b++ }
    }
    if a > b { return a }
    return b
}
