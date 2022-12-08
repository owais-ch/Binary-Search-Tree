'''
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

Example 1:

Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.
'''

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def traversal(root):
            nonlocal total,count

            if root==None:
                return None

            total+=root.val
            
            if total==targetSum:
                count+=1
                
           
            if total-targetSum in dict1:
                count+=dict1[total-targetSum]
                
            
            if total not in dict1:
                dict1[total]=1
            else:
                dict1[total]+=1
            

            if traversal(root.left) or traversal(root.right):
                return True

            if dict1[total]==1:
                dict1.pop(total)
            else:
                dict1[total]-=1

            total-=root.val

            return False

        total,count=0,0
        dict1=dict()
        
        traversal(root)

        return count
