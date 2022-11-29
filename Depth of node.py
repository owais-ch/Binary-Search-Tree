'''
Given a binary tree, find the depth of the deepest odd level leaf node in a binary tree. If there is no leaf at odd level then return 0.
Consider that level starts with 1. Depth of a leaf node is number of nodes on the path from root to leaf (including both leaf and root).

Example 1:

Input: 
          1
        /    \
       2      3
      / \    / \
     4   5  6   7
Output: 3
Explanation: In the above tree 4,5,6 and 7 are
odd level leaf nodes at depth 3.So the answer is 3.
'''

class Solution:
    def depthOfOddLeaf(self,root):
        def traversal(root,level):
            nonlocal maximum
            if root==None:
                return None
                
            if level%2!=0 and root.left==None and root.right==None:
                maximum=max(maximum,level)
                
            if root.left:
                traversal(root.left,level+1)
            
            if root.right:
                traversal(root.right,level+1)
        
        maximum=-99        
        traversal(root,1)
        
        if maximum==-99:
            return 0
        
        return maximum
