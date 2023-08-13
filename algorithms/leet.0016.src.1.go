// https://leetcode.cn/problems/3sum-closest/description/
// 16. 最接近的三数之和

func threeSumClosest(nums []int, target int) int {
    diff := -1
    ans := -1
    n := len(nums)
    for i:=0; i<n; i+=1 {
        for j:=i+1; j<n; j+=1 {
            for k:=j+1; k<n; k++ {
                s := nums[i] + nums[j] + nums[k]
                d := target - s
                if s - target > d {
                    d = s - target
                }
                if diff == -1 || d < diff {
                    diff = d
                    ans = s
                }
            }
        }
    }
    return ans
}
