'''You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.
Example 1:
Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]'''

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def traversal(root1,root2,level):
            if root1==None or root2==None:
                return None
            
            if level==0:
                if root1.left and root2.left:
                    root1.left.val=root1.left.val+root2.left.val
                elif root1.left==None and root2.left:
                    root1.left=TreeNode(root2.left.val)
                    
                if root1.right and root2.right:
                    root1.right.val=root1.right.val+root2.right.val
                elif root1.right==None and root2.right:
                    root1.right=TreeNode(root2.right.val)
                    
            else:
                traversal(root1.left,root2.left,level-1)
                traversal(root1.right,root2.right,level-1)
                
        def height(root):
            if root==None:
                return 0
            
            left=height(root.left)
            right=height(root.right)
            
            return max(left,right)+1
        
        tall1=height(root1)
        tall2=height(root2)
        
        tall=min(tall1,tall2)
        
        for i in range(tall):
            traversal(root1,root2,i)
        if root1==None and root2:
            root1=root2
        elif root1 and root2:
            root1.val=root1.val+root2.val    
        return root1
