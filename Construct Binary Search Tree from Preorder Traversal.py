'''Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), construct the tree and return its root.

It is guaranteed that there is always possible to find a binary search tree with the given requirements for the given test cases.

A binary search tree is a binary tree where for every node, any descendant of Node.left has a value strictly less than Node.val, and any descendant of Node.right
has a value strictly greater than Node.val.

A preorder traversal of a binary tree displays the value of the node first, then traverses Node.left, then traverses Node.right.

 

Example 1:


Input: preorder = [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]'''


class Solution:
    def bstFromPreorder(self, preorder): 
        m=TreeNode(preorder[0])
        root=m
        
        def insert(m,data):
            if m.val>data:
                if m.left:
                    insert(m.left,data)
                else:
                    m.left=TreeNode(data)
                    
            else:
                if m.right:
                    insert(m.right,data)
                else:
                     m.right=TreeNode(data)
                    
        for i in range(1,len(preorder)):
            insert(m,preorder[i])
            
        return root
