'''You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

Example 1:


Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]'''

class Solution:
    def searchBST(self, root, val):
        if val==root.val:
            return root
        
        if root.val>val:
            if root.left:
                return self.searchBST(root.left,val)
                
        elif root.val<val:
            if root.right:
                return self.searchBST(root.right,val)
        return None
