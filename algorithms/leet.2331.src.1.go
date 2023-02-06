// https://leetcode.cn/problems/evaluate-boolean-binary-tree/
// 2331. 计算布尔二叉树的值 - 简单递归

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func evaluateTree(root *TreeNode) bool {
    if root.Left == nil { return root.Val != 0 }
    if root.Val == 2 { return evaluateTree(root.Left) || evaluateTree(root.Right) }
    return evaluateTree(root.Left) && evaluateTree(root.Right)
}
