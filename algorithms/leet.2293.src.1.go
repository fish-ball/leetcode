// https://leetcode.cn/problems/min-max-game/
// 2293. 极大极小游戏 - 简单模拟

func minMaxGame(nums []int) int {
    for len(nums) > 1 {
        for i:=0; i+i<len(nums); i++ {
            if i % 2 == 0 {
                if nums[i+i] < nums[i+i+1] {
                    nums[i] = nums[i+i]
                } else {
                    nums[i] = nums[i+i+1]
                }
            } else {
                if nums[i+i] > nums[i+i+1] {
                    nums[i] = nums[i+i]
                } else {
                    nums[i] = nums[i+i+1]
                }
            }
        }
        nums = nums[:len(nums)/2]
    }
    return nums[0]
}
