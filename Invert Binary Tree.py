'''Given the root of a binary tree, invert the tree, and return its root.

Example 1:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]'''

class Solution:
    def __init__(self):
        self.list1=[]
    def invertTree(self, root):
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
                if root.left and root.right:
                    root.left,root.right=root.right,root.left
                elif root.left and root.right==None:
                    root.right=root.left
                    root.left=None
                elif root.right and root.left==None:
                    root.left=root.right
                    root.right=None
            else:
                traversal(root.left,level-1)
                traversal(root.right,level-1)
        if root==None:
            return None
        
        tall1=height(root.left)
        tall2=height(root.right)
        
        tall=max(tall1,tall2)
        
        for i in range(tall):
            traversal(root,i)
        return root
        
