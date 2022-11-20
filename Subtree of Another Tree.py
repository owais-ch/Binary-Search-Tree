'''Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of 
itself.

Example 1:

Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true'''

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def traversal(root):
            nonlocal parent

            if root==None:
                return None
            if root.val==subRoot.val:
                parent.append(root)
                #return

            if root.left:
                traversal(root.left)
            if root.right:
                traversal(root.right)

        parent=[]
        traversal(root)
        if parent==[]:
            return False

        def is_identical(root1,root2):
            if root1==None and root2==None:
                return True
            elif root1!=None and root2!=None and root1.val==root2.val:
                return is_identical(root1.left,root2.left) and is_identical(root1.right,root2.right)
            else:
                return False
        
        for i in parent:
            value=is_identical(i,subRoot)
            if value==True:
                return True
        return False
