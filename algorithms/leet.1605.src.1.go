// https://leetcode.cn/problems/find-valid-matrix-given-row-and-column-sums/
// 1605. 给定行和列的和求可行矩阵

func restoreMatrix(rowSum []int, colSum []int) [][]int {
    n := len(rowSum)
    m := len(colSum)
    mat := [][]int{}
    for i:=0; i<n; i++ {
        mat = append(mat, make([]int, m))
    }
    for i,j:=0,0; i<n&&j<m; {
        if rowSum[i]>colSum[j] {
            mat[i][j] += colSum[j]
            rowSum[i] -= colSum[j]
            colSum[j] = 0
        } else {
            mat[i][j] += rowSum[i]
            colSum[j] -= rowSum[i]
            rowSum[i] = 0
        }
        if rowSum[i]==0 { i++ }
        if colSum[j]==0 { j++ }
    }
    return mat
}
