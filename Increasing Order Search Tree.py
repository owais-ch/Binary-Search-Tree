'''Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left 
child and only one right child.

Example 1:

Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]'''

class Solution:
    def __init__(self):
        self.list1=[]
    def increasingBST(self, root):
        def traversal(root):
            if root.left:
                traversal(root.left)
                
            self.list1.append(root.val)
            
            if root.right:
                traversal(root.right)
                
        traversal(root)
        
        self.list1.sort()
        
        length=len(self.list1)
        
        m=TreeNode(self.list1[0])
        
        head=m
        
        for i in range(1,length):
            hh=TreeNode(self.list1[i])
            m.right=hh
            m=m.right
            
        return head
