// https://leetcode.cn/problems/merge-k-sorted-lists/
// 23. 合并 K 个升序链表

type Heap []*ListNode

func (h Heap) Len() int { return len(h) }
func (h Heap) Less(i, j int) bool { 
    if h[i] == nil { return true }
    if h[j] == nil { return false }
    return h[i].Val < h[j].Val
}
func (h Heap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }
func (h *Heap) Push(x interface{}) { *h = append(*h, x.(*ListNode)) }
func (h *Heap) Pop() interface{} {
    n := len(*h)
    x := (*h)[n-1]
    *h = (*h)[:n-1]
    return x
}

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeKLists(lists []*ListNode) *ListNode {
    h := Heap(lists)
    heap.Init(&h)
    var head *ListNode = nil
    var ans *ListNode = nil
    for len(h) > 0 {
        ls := heap.Pop(&h).(*ListNode)
        if ls == nil { continue }
        if head == nil {
            ans = ls
            head = ans
        } else {
            ans.Next = ls
            ans = ls
        }
        ls = ls.Next
        if ls != nil {
            heap.Push(&h, ls)
        }
    }
    return head
}
