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
    public int minDepth(TreeNode root) {
        if(root == null) return 0;
        if(root.left == null && root.right == null) return 1;
        int x = root.left == null ? 999999999 : minDepth(root.left);
        int y = root.right == null ? 999999999 : minDepth(root.right);
        return Math.min(x, y) + 1;
    }
}
