// https://leetcode.cn/problems/merge-similar-items/
// 2363. 合并相似的物品

func mergeSimilarItems(items1 [][]int, items2 [][]int) [][]int {
    a := make([]int, 1001)
    for _, x := range items1 {
        a[x[0]] += x[1]
    }
    for _, x := range items2 {
        a[x[0]] += x[1]
    }
    ans := [][]int{}
    for i, x := range a {
        if x > 0 {
            ans = append(ans, []int{i, x})
        }
    }
    return ans
}
