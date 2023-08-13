// https://leetcode.cn/problems/4sum/description/
// 18. 四数之和

func fourSum(nums []int, target int) [][]int {
    sort.Ints(nums)
    ans := [][]int{}
    n := len(nums)
    d := map[int]bool{}
    for i:=0; i<n; i++ {
        for j:=i+1; j<n; j++ {
            for k:=j+1; k<n; k++ {
                for l:=k+1; l<n; l++ {
                    if nums[i] + nums[j] + nums[k] + nums[l] == target {
                        hash := ((nums[i]*99991+nums[j])*99991+nums[k])*99991+nums[l]
                        if !d[hash]  {
                            ans = append(ans, []int{nums[i], nums[j], nums[k], nums[l]})
                            d[hash] = true
                        }
                    }
                }
            }
        }
    }
    return ans
}
