/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode insertionSortList(ListNode head) {
        if(head == null) return null;
        ListNode ans = head, p, q;
        head = ans.next;
        ans.next = null;
        while(head != null) {
            p = head;
            head = p.next;
            if(p.val <= ans.val) {
                p.next = ans;
                ans = p;
            }
            else {
                q = ans;
                while(q.next != null && q.next.val < p.val) {
                    q = q.next;
                }
                p.next = q.next;
                q.next = p;
            }
        }
        return ans;
        
    }
}
