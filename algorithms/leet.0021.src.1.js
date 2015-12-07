/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var mergeTwoLists = function(l1, l2) {
    var head = new ListNode(0), current = head;
    while(l1 || l2) {
        if(!l1 || l2 && l1.val > l2.val) {
            var tmp = l1;
            l1 = l2;
            l2 = tmp;
        }
        current.next = l1;
        current = current.next;
        l1 = l1.next;
    }
    return head.next;
};
