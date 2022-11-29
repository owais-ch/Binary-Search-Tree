'''Given a Binary Tree of N nodes. Find the vertical width of the tree.

Example 1:

Input:
          1
       /    \
      2      3
     / \    / \
    4   5  6   7
            \   \
             8   9
Output: 6
Explanation: The width of a binary tree is
the number of vertical paths in that tree.'''


def verticalWidth(root):
    def traversal(root,level):
        nonlocal maximum,minimum
        if root==None:
            return 0
            
        maximum=max(maximum,level)
        minimum=min(minimum,level)
        
        if root.left:
            traversal(root.left,level-1)
            
        if root.right:
            traversal(root.right,level+1)
            
    minimum=0
    maximum=-1
    
    traversal(root,0)
    
    return maximum-minimum+1
