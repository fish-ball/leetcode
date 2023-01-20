// https://leetcode.cn/problems/finding-the-users-active-minutes/
// 1817. 查找用户活跃分钟数
func findingUsersActiveMinutes(logs [][]int, k int) []int {
    mps := map[int]map[int]bool{}
    for _, log := range logs {
        if _, ok := mps[log[0]]; !ok {
            mps[log[0]] = map[int]bool{}
        }
        mps[log[0]][log[1]] = true
    }
    ans := make([]int, k, k)
    for _, mp := range mps { 
        val := len(mp)
        if 1 <= val && val <= k { ans[val - 1]++ }
    }
    return ans
}
