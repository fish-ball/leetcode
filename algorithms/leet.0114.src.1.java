/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public void flatten(TreeNode root) {
        if(root == null) return;
        TreeNode left = root.left;
        TreeNode right = root.right;
        TreeNode next = root;
        if(left != null) {
            flatten(left);
            root.left = null;
            root.right = left;
            next = left;
            while(next.right != null) next = next.right;
        }
        if(right != null) {
            flatten(right);
            next.right = right;
        }
    }
}
