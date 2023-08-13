// https://leetcode.cn/problems/remove-nth-node-from-end-of-list/description/
// 19. 删除链表的倒数第 N 个结点

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeNthFromEnd(head *ListNode, n int) *ListNode {
    p := head
    for i:=0; i<=n; i++ {
        if p == nil {
            return head.Next
        }
        p = p.Next
    }
    q := head
    for ; p != nil; p = p.Next {
        q = q.Next
    }
    q.Next = q.Next.Next
    return head
}
