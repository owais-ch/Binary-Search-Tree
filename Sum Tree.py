'''Given a Binary Tree. Return true if, for every node X in the tree other than the leaves, its value is equal to the sum of its left subtree's value and its right subtree's value.
Else return false.

An empty tree is also a Sum Tree as the sum of an empty tree can be considered to be 0. A leaf node is also considered a Sum Tree.


Example 1:

Input:
    3
  /   \    
 1     2

Output: 1'''

class Solution:
    def isSumTree(self,root):
        def traversal(root):
            nonlocal total_sum
            
            if root==None:
                return None
            
            total_sum+=root.data    
            
            if root.left:
                traversal(root.left)
                
            if root.right:
                traversal(root.right)
                
        def traversal2(root):
            nonlocal total_sum,output
            total_sum=0
            if root==None:
                return None
            elif root.left==None and root.right==None:
                output=True
                return 
            traversal(root)
            
            if total_sum-root.data!=root.data:
                
                output=False
                
                return
            
            if root.left:
                traversal2(root.left)
                
            if root.right:
                traversal2(root.right)
                
        output=True
        total_sum=0
        traversal2(root)
        
        return output
