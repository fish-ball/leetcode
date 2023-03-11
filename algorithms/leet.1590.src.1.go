// https://leetcode.cn/problems/make-sum-divisible-by-p/
// 1590. 使数组和能被 P 整除

func minSubarray(nums []int, p int) int {
    s := 0
    ans := -1
    mp := map[int]int{0:-1}
    for _, x := range nums {
        s += x
        s %= p
    }
    if s == 0 { return 0 }
    t := 0
    for i, x := range nums {
        t += x
        t %= p
        k := (p+t-s) % p
        if j, ok := mp[k]; ok && (ans<0 || ans>i-j) && i-j<len(nums) { ans = i-j }
        mp[t] = i
    }
    return ans
}
