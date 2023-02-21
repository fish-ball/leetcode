// https://leetcode.cn/problems/minimum-number-of-taps-to-open-to-water-a-garden/
// 1326. 灌溉花园的最少水龙头数目
// 先将区间排序然后贪心即可
type RangeArray [][]int

func (a RangeArray) Len() int { return len(a) }
func (a RangeArray) Less(i, j int) bool { return a[i][0] < a[j][0] }
func (a RangeArray) Swap(i, j int) { a[i], a[j] = a[j], a[i] }

func minTaps(n int, ranges []int) int {
    a := RangeArray{}
    for i, x := range ranges {
        if x == 0 { continue }
        a = append(a, []int{i-x, i+x})
    }
    sort.Sort(a)
    // fmt.Println(a)
    left := 0
    right := 0
    ans := 0
    for _, rng := range(a) {
        // fmt.Println(left, right, rng, ans)
        if rng[0] > left && rng[0] <= right {
            left = right
            ans++
        }
        if rng[0] <= left && rng[1] > right {
            right = rng[1]
        }
    }
    if left >= n { return ans }
    if right >= n { return ans + 1 }
    return -1
}
