// https://leetcode.cn/problems/minimum-operations-to-reduce-x-to-zero/
// 双指针，先定位右侧 j 的极限，然后枚举左区间 i，每次让 j 右移到极限。
func minOperations(nums []int, x int) int {
    n := len(nums)
    sum := 0
    for _, a := range nums {
        sum += a
    }
    j := n
    ans := -1
    for ; j > 0 && x - nums[j-1] >= 0; j-- {
        x -= nums[j-1]
    }
    if x == 0 {
        ans = n - j
    }
    for i, a := range nums {
        for x -= a; j <= i || x < 0 && j < n; j++ {
            x += nums[j]
        }
        if x == 0 && (ans == -1 || ans > n - j + i + 1) {
            ans = n - j + i + 1
        }
    }
    return ans
}
