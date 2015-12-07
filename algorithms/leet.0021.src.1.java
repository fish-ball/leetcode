/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(0), current = head;
        while(l1 != null || l2 != null) {
            if(l1 == null || l2 != null && l1.val > l2.val) {
                ListNode tmp = l1;
                l1 = l2;
                l2 = tmp;
            }
            current.next = l1;
            current = current.next;
            l1 = l1.next;
        }
        return head.next;
    }
}
