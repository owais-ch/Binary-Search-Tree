'''You are given a binary tree. Your task is pretty straightforward. You have to find the sum of the product of each node and its mirror image (The mirror of a node is 
 a node which exists at the mirror position of the node in opposite subtree at the root.). Don’t take into account a pair more than once. The root node is the mirror 
image of itself.

 

Example 1:

Input:
      4         
    /    \
   5      6
Output:
46
Explanation:
Sum = (4*4) + (5*6) = 46
'''
class Solution:
    # your task is to complete this function
    def imgMultiply(self, root):
        def pro(root1,root2):
            nonlocal sum1
            
            if root1==None or root2==None:
                return 0
            
            sum1+=root1.data*root2.data
            pro(root1.left,root2.right)
            pro(root1.right,root2.left)
            
        sum1=0
        
        pro(root.left,root.right)
        
        sum1+=(root.data**2)
            
        return sum1%(10**9+7)

