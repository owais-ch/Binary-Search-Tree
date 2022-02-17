'''Given a Binary Tree, convert it into its mirror.'''

class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self,root):
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
                elif root.left==None and root.right:
                    root.left=root.right
                    root.right=None
                elif root.left and root.right==None:
                    root.right=root.left
                    root.left=None
            else:
                traversal(root.left,level-1)
                traversal(root.right,level-1)
                
        tall=height(root)
        
        for i in range(tall):
            traversal(root,i)
            
        return root
