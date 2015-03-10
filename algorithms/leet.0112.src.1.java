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
    boolean result;
    int s, t;
    public boolean hasPathSum(TreeNode root, int sum) {
        result = false;
        s = 0;
        t = sum;
        dfs(root);
        return result;
    }
    void dfs(TreeNode p) {
        if(p == null) return;
        s += p.val;
        if(p.left == null && p.right == null && s == t) result = true;
        dfs(p.left);
        dfs(p.right);
        s -= p.val;
    }
    
}
