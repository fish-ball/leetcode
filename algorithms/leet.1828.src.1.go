// https://leetcode.cn/problems/queries-on-number-of-points-inside-a-circle/
// 1828. 统计一个圆中点的数目 - 字面意思，暴力即可
func countPoints(points [][]int, queries [][]int) []int {
    ans := make([]int, len(queries))
    for i:=0; i<len(queries); i++ {
        q := queries[i]
        x, y, r := q[0], q[1], q[2]
        for j:=0; j<len(points); j++ {
            p := points[j]
            xx, yy := p[0], p[1]
            if (x-xx)*(x-xx)+(y-yy)*(y-yy) <= r*r {
                ans[i]++
            }
        }
    }
    return ans
}
