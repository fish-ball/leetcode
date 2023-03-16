// https://leetcode.cn/problems/count-subarrays-with-median-k/
// 2488. 统计中位数为 K 的子数组
// 水位法

func countSubarrays(nums []int, k int) int {
    seen := false
    mp_odd := map[int]int{0: 1}
    mp_even := map[int]int{}
    acc := 0
    ans := 0
    for i, x := range nums {
        if x == k {
            seen = true
        } else if x > k {
            acc++
        } else {
            acc--
        }
        // fmt.Println(x, acc, seen)
        // fmt.Println("  odd", mp_odd)
        // fmt.Println("  event", mp_even)
        if seen {
            if i % 2 > 0 {
                // fmt.Println("  ^", mp_odd[acc-1], mp_even[acc])
                ans += mp_odd[acc-1] + mp_even[acc]
            } else {
                // fmt.Println("  !", mp_odd[acc], mp_even[acc-1])
                ans += mp_odd[acc] + mp_even[acc-1]
            }
        } else {
            if i%2==0 { mp_even[acc]++ } else { mp_odd[acc]++ }
        }
        // fmt.Println("ans =", ans)
    }
    return ans
}
