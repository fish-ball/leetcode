// https://leetcode.cn/problems/merge-in-between-linked-lists/
// 1669. 合并两个链表

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeInBetween(list1 *ListNode, a int, b int, list2 *ListNode) *ListNode {
    p, q := list1, list1
    for i:=1; i<a; i++ { p = p.Next }
    for i:=0; i<=b; i++ { q = q.Next }
    p.Next = list2
    for p = list2; p.Next != nil; { p = p.Next }
    p.Next = q
    return list1
}
