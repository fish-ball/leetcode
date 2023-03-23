// https://leetcode.cn/problems/arithmetic-subarrays/submissions/
// 1630. 等差子数组

func checkArithmeticSubarrays(nums []int, l []int, r []int) []bool {
    ans := []bool{}
    for i, _ := range l {
        arr := nums[l[i]:r[i]+1]
        min := arr[0]
        max := arr[0]
        for _, x := range arr {
            if x < min { min = x }
            if x > max { max = x }
        }
        if min == max { 
            ans = append(ans, true)
            continue
        }
        if (max - min) % (len(arr) - 1) > 0 {
            ans = append(ans, false)
            continue
        }
        d := (max - min) / (len(arr) - 1)
        yes := true
        b := make([]bool, len(arr))
        for _, x := range arr {
            if (x - min) % d > 0 {
                yes = false
                break
            }
            k := (x - min) / d
            if b[k] {
                yes = false
                break
            }
            b[k] = true
        }
        ans = append(ans, yes)
    }
    return ans
}
