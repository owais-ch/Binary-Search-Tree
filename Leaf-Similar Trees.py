'''Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.'''

class Solution:
    def leafSimilar(self, root1, root2) -> bool:
        def traversal(root,list1):
            if root==None:
                return None
            elif root.left==None and root.right==None:
                list1.append(root.val)
                
            if root.left:
                traversal(root.left,list1)
                
            if root.right:
                traversal(root.right,list1)
        list1=[] 
        list2=[]
        traversal(root1,list1)
        traversal(root2,list2)
        if list1==list2:
            return True
        else:
            return False
