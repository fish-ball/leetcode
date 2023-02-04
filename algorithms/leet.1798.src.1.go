// https://leetcode.cn/problems/maximum-number-of-consecutive-values-you-can-make/
// 1798. 你能构造出连续值的最大数目
// 贪心：挺有意思的，排序，先从小开始，每加入一个数就能达到最多连到 sum(a[0..i])
// 断开的条件在于：
// 到某个 i 的时候，如果 a[i] > sum(a[0..i-1]) + 1
// 说明 sum(a[0..i-1])+1 这个数是绝对凑不出来了

type Arr []int
func (a Arr) Len() int { return len(a) }
func (a Arr) Less(i, j int) bool { return a[i] < a[j] }
func (a Arr) Swap(i, j int) { a[i], a[j] = a[j], a[i] }

func getMaximumConsecutive(coins []int) int {
    sort.Sort(Arr(coins))
    p := 0
    for _, x := range coins {
        if x > p+1 { break }
        p += x
    }
    return p + 1
}
