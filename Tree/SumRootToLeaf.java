/*
LC 129

You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

*/


class SumRootToLeaf {
    
    public int sumRootToLeaf(TreeNode root, int sum){
        
        int result = 0;
        if(root == null)
            return sum;
        if(root.left == null && root.right == null){
            return sum*10 + root.val;
        }
        
        if (root.left != null)
            result +=  sumRootToLeaf(root.left, sum*10 + root.val);
        if (root.right != null)
            result += sumRootToLeaf(root.right, sum*10 + root.val);
        
        return result;
    }
    public int sumNumbers(TreeNode root) {
        int sum = 0;
        
        return sumRootToLeaf(root, sum);
        
    }
}