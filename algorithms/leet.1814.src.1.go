// https://leetcode.cn/problems/count-nice-pairs-in-an-array/
// 1814. 统计一个数组中好对子的数目
// 稍为变换一下公式，编程 nums[i]-rev(nums[i]) 相同的对数
func countNicePairs(nums []int) int {
    ans := int64(0)
    mp := map[int]int64{}
    for _, x := range nums {
        z := 0
        for y := x; y > 0; y /= 10 { z = z * 10 + y % 10 }
        ans += mp[x-z]
        ans %= 1000000007
        mp[x-z]++
    }
    return int(ans)
}
