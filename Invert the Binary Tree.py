'''Problem Description

Given a binary tree A, invert the binary tree and return it. 

 Inverting refers to making left child as the right child and vice versa.
 
 Input 1

     1
   /   \
  2     3
 / \   / \
4   5 6   7

Output 1:

 
     1
   /   \
  3     2
 / \   / \
7   6 5   4
 '''
class Solution:
	def invertTree(self, root):
        if root==None:
            return 
        root.left,root.right=root.right,root.left

        root.left=self.invertTree(root.left)
        root.right=self.invertTree(root.right)

        return root
