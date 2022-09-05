/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
const P1 = 213023
const P2 = 130279

var a []*TreeNode
var mp map[int]int

func findDuplicateSubtrees(root *TreeNode) []*TreeNode {
    a = make([]*TreeNode, 0)
    mp = make(map[int]int)
    dfs(root)
    return a
}

func dfs(nd *TreeNode) int {
    if (nd == nil) {
        return 0
    }
    hash := nd.Val + 9999 + (dfs(nd.Left)+P1) * (dfs(nd.Right)+P2)
    cnt, ok := mp[hash]
    if (ok) {
        mp[hash] += 1
        if(cnt == 1) {
            a = append(a, nd)
        }
    } else {
        mp[hash] = 1
    }
    return hash
}
