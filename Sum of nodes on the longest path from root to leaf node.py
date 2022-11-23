'''Given a binary tree of size N. Your task is to complete the function sumOfLongRootToLeafPath(), that find the sum of all nodes on the longest path from 
root to leaf node.
If two or more paths compete for the longest path, then the path having maximum sum of nodes is being considered.

Example 1:

Input: 
        4        
       / \       
      2   5      
     / \ / \     
    7  1 2  3    
      /
     6
Output: 13
Explanation:
        4        
       / \       
      2   5      
     / \ / \     
    7  1 2  3 
      /
     6

The highlighted nodes (4, 2, 1, 6) above are 
part of the longest root to leaf path having
sum = (4 + 2 + 1 + 6) = 13'''


class Solution:
    def sumOfLongRootToLeafPath(self,root):
        def traversal(root):
            nonlocal count,total,maximum,max_total
            
            if root==None:
                return None
                
            total+=root.data
            count+=1
            
            if root.left==None and root.right==None:
                if count>maximum:
                    maximum=count
                    max_total=total
                elif count==maximum and total>max_total:
                    max_total=total
                    
            if traversal(root.left) or traversal(root.right):
                return True
                
            total-=root.data
            count-=1
            
        count=0
        total=0
        maximum=-9999
        max_total=-9999
        
        traversal(root)
        
        return max_total
