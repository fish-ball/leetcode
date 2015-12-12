/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function(root, k) {
    var idx = 0, result = null;
    var walk = function(ptr) {
        if(result !== null) return;
        if(ptr.left) walk(ptr.left);
        if(++idx == k) result = ptr.val;
        if(ptr.right) walk(ptr.right);
    };
    walk(root);
    return result;
};
