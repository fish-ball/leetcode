// https://leetcode.cn/problems/count-subtrees-with-max-distance-between-cities/submissions/
// 1617. 统计子树中城市之间最大距离
// 暴力枚举掩码，判断树，计算直径，关键是计算直径的算法：从一个节点出发找到最远的节点，再从那个节点出发找最远的节点。


func countSubgraphsForEachDiameter(n int, edges [][]int) []int {
    for _, e := range edges { 
        e[0]--
        e[1]--
    }

    // 结果数组
    ans := make([]int, n-1)

    // 直接枚举掩码
    for mask:=1; mask<(1<<n); mask++ {
        // 先判断是不是树，不是的话排除
        // 先录入所有的涉及顶点
        vv := []int{}
        for v:=0; v<n; v++ {
            if (1<<v)&mask > 0 {
                vv = append(vv, v)
            }
        }
        // 这种情况是直径==0的，跳过
        if len(vv) < 2 { continue }
        // fmt.Println(vv)
        // 遍历所有边，要是刚好命中 len(vv)-1 条边说明是树
        ee := [][]int{}
        for _, e := range edges {
            if (1<<e[0])&mask>0 && (1<<e[1])&mask>0 {
                ee = append(ee, e)
            }
        }
        if len(ee) != len(vv) - 1 { continue }
        // fmt.Println(' ', vv, ee)
        // 是的话算出树的直径 d，再加到结果里面
        // 计算直径第一步，先求出任意一个点出发的最远点
        visited := make([]bool, n)
        v := ee[0][0]
        visited[v] = true
        for {
            found := false
            visited2 := make([]bool, n)
            copy(visited2, visited)
            for _, e := range ee {
                if visited[e[0]] && !visited[e[1]] {
                    found = true
                    visited2[e[1]] = true
                    v = e[1]
                } else if visited[e[1]] && !visited[e[0]] {
                    found = true
                    visited2[e[0]] = true
                    v = e[0]
                }
            }
            if !found { break }
            visited = visited2
        }
        // 再从这个最远点出发求最远点
        d := 0
        visited = make([]bool, n)
        visited[v] = true
        for {
            found := false
            visited2 := make([]bool, n)
            copy(visited2, visited)
            for _, e := range ee {
                if visited[e[0]] && !visited[e[1]] {
                    found = true
                    visited2[e[1]] = true
                    v = e[1]
                } else if visited[e[1]] && !visited[e[0]] {
                    found = true
                    visited2[e[0]] = true
                    v = e[0]
                }
            }
            if !found { break }
            visited = visited2
            d++
        }
        ans[d-1]++
    }

    return ans
}
