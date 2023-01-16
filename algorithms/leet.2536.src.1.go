// https://leetcode.cn/problems/increment-submatrices-by-one/
// 二维矩阵差分，可以将最终的矩阵看做矩阵的累加和矩阵，这样的话每画一个新的矩阵，只需要记录四个差分值就行
// 最后做一次累计和即可，O(n^2)
func rangeAddQueries(n int, queries [][]int) [][]int {
    acc := make([][]int, n, n)
    for i:=0; i<n; i++ { acc[i] = make([]int, n, n) }
    for _, q := range queries {
        acc[q[0]][q[1]] += 1
        if q[3]<n-1 { acc[q[0]][q[3]+1] -= 1 }
        if q[2]<n-1 { acc[q[2]+1][q[1]] -= 1 }
        if q[2]<n-1 && q[3]<n-1 { acc[q[2]+1][q[3]+1] += 1 }
    }
    for i:=0; i<n; i++ {
        for j:=0; j<n; j++ {
            if i>0 && j>0 { acc[i][j] -= acc[i-1][j-1] }
            if i>0 { acc[i][j] += acc[i-1][j] }
            if j>0 { acc[i][j] += acc[i][j-1] }
        }
    }
    return acc
}
