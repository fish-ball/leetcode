// https://leetcode.cn/problems/make-array-zero-by-subtracting-equal-amounts/
// 2357. 使数组中所有元素都等于零

func minimumOperations(nums []int) int {
    mp := map[int]bool{}
    for _, x:= range nums {
        if x > 0 { mp[x] = true }
    }
    return len(mp)
}
