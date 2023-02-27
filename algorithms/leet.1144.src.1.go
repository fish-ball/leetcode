// https://leetcode.cn/problems/decrease-elements-to-make-array-zigzag/
// 1144. 递减元素使数组呈锯齿状

func movesToMakeZigzag(nums []int) int {
    n := len(nums)
    a, b := 0, 0
    // 第一轮，先升后降
    for i:=0; i<n; i+=2 {
        x := nums[i]
        if i>0 && nums[i-1]<=x { x = nums[i-1] - 1 }
        if i<n-1 && nums[i+1]<=x { x = nums[i+1] - 1 }
        a += nums[i]-x
    }
    // 第二轮，反过来
    for i:=1; i<n; i+=2 {
        x := nums[i]
        if nums[i-1]<=x { x = nums[i-1] - 1 }
        if i<n-1 && nums[i+1]<=x { x = nums[i+1] - 1 }
        b += nums[i]-x
    }
    if a < b { return a } else { return b }
}
