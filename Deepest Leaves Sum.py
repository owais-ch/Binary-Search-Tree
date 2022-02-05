'''Given the root of a binary tree, return the sum of values of its deepest leaves.
 
Example 1:

Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15'''


class Solution:
    def __init__(self):
        self.total=0
        self.list1=[]
    def deepestLeavesSum(self, root) -> int:
        def height(root):
            if root==None:
                return 0
            left=height(root.left)
            right=height(root.right)
            
            return max(left,right)+1
            
            
        def level_order(root,level):
            if root==None:
                return 
            if level==0:
                self.list1.append(root.val)
            else:
                level_order(root.left,level-1)
                level_order(root.right,level-1)
            
        tall=height(root)
        
        
        level_order(root,tall-1)
        self.total=sum(self.list1)
        
        return self.total
