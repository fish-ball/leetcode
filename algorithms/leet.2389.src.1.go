// https://leetcode.cn/problems/longest-subsequence-with-limited-sum/
// 2389. 和有限的最长子序列

type IntArray []int
func (arr IntArray) Len() int { return len(arr) }
func (arr IntArray) Less(i, j int) bool { return arr[i] < arr[j] }
func (arr IntArray) Swap(i, j int) { arr[i], arr[j] = arr[j], arr[i] }

func answerQueries(nums []int, queries []int) []int {
    ans := []int{}
    sort.Sort(IntArray(nums))
    for i:=1; i<len(nums); i++ {
        nums[i] += nums[i-1]
    }
    for _, q := range queries {
        left := -1
        right := len(nums)
        for left+1 < right {
            middle := (left + right) / 2
            if nums[middle] <= q { left = middle } else { right = middle }
        }
        ans = append(ans, right)
    }
    return ans
}
