import java.util.*;
import java.io.*;
import java.lang.*;

class DepthOfTree{

}

//Definition for a binary tree node.

// 

 //LC 104
class MaxDepth {
    public int maxDepth(TreeNode root) {
        
        if(root == null)
            return 0;
        
        int maxLevel = 0;
        
        Queue<TreeNode> q = new LinkedList();
        Queue<Integer> qLevel = new LinkedList();
        
        q.add(root);
        qLevel.add(1);
        
        TreeNode temp;
        int level;
        
        
        while( !q.isEmpty() ){
            temp = q.poll();
            level = qLevel.poll();
            
            maxLevel = Math.max(maxLevel, level);
            
            if(temp.left != null){
                q.add(temp.left);
                qLevel.add(level+1);
            }
            
            if(temp.right != null){
                q.add(temp.right);
                qLevel.add(level+1);
            }
        }
        
        return maxLevel;
    }
}

//LC 111

class MinDepth {
    public int minDepth(TreeNode root) {
        
        if(root == null)
            return 0;
        
        int minLevel = Integer.MAX_VALUE;
        
        Queue<TreeNode> q = new LinkedList();
        Queue<Integer> qLevel = new LinkedList();
        
        TreeNode temp;
        int level;
        
        q.add(root);
        qLevel.add(1);
        
        while( !q.isEmpty() ){
            temp = q.poll();
            level = qLevel.poll();
            
            if(temp.left == null && temp.right == null){
                minLevel = Math.min(minLevel, level);
                continue;
            }
            
            if(temp.left != null){
                q.add(temp.left);
                qLevel.add(level+1);
            }
            
            if(temp.right != null){
                q.add(temp.right);
                qLevel.add(level+1);
            }
        }
        
        return minLevel;
        
    }
}