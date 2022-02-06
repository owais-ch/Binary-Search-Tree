'''Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

Example 1:

Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]'''

class Solution:
    def __init__(self):
        self.list1=[]
    def largestValues(self, root) -> List[int]:
        def height(root):
            if root==None:
                return 0
            
            left=height(root.left)
            right=height(root.right)
            
            return max(left,right)+1
        
        def traversal(root,level):
            if root==None:
                return None
            if level==0:
                self.list1.append(root.val)
            else:
                traversal(root.left,level-1)
                traversal(root.right,level-1)
                
        tall=height(root)
        list2=[]
        
        for i in range(tall):
            traversal(root,i)
            list2.append(max(self.list1))
            self.list1=[]
            
        return list2
