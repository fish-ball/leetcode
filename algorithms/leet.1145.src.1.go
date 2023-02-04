// https://leetcode.cn/problems/binary-tree-coloring-game/
// 1145. 二叉树着色游戏
// 找到给定的 x 节点，这个节点会将树割成三份，在这三份中只要有一份过半就赢了

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func btreeGameWinningMove(root *TreeNode, n int, x int) bool {
    mp := map[int]int{}
    var nodex *TreeNode = nil
    var dfs func(nd *TreeNode)int
    dfs = func(nd *TreeNode) int {
        if nd == nil { return 0; }
        if nd.Val == x { nodex = nd }
        a := dfs(nd.Left) + dfs(nd.Right) + 1
        mp[nd.Val] = a
        return a
    }
    dfs(root)
    xx := mp[root.Val]
    y1, y2 := 0, 0
    if nodex.Left != nil { y1 = mp[nodex.Left.Val] }
    if nodex.Right != nil { y2 = mp[nodex.Right.Val] }
    y := xx - y1 - y2 - 1
    if y1 > y { y = y1 }
    if y2 > y { y = y2 }
    return y > xx - y
}
