'''Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 2'''

class Solution:
    def minDepth(self, root) -> int:
        def height(root):
            if root==None:
                return 0
            
            left=height(root.left)
            right=height(root.right)
            
            return max(left,right)+1
        
        def traversal(root,level):
            nonlocal output
            if root==None:
                return None
            elif root.left==None and root.right==None:
                output=-1
                
                return
            
            if level==0:
                pass
            else:
                traversal(root.left,level-1)
                traversal(root.right,level-1)
                
        tall=height(root)
        if tall==0:
            return 0
        output=0
        for i in range(tall):
            traversal(root,i)
            if output==-1:
                return i+1
