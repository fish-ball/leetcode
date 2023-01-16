// https://leetcode.cn/problems/difference-between-element-sum-and-digit-sum-of-an-array/
// 2535. 数组元素和与数字和的绝对差
func differenceOfSum(nums []int) int {
    s1 := 0
    s2 := 0
    for _, x := range nums { 
        s1 += x 
        for ; x > 0; x /= 10 { s2 += x % 10 }
    }
    if s1 > s2 { return s1 - s2 }
    return s2 - s1
}
