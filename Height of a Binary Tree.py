'''The height of a binary tree is the number of edges between the tree's root and its furthest leaf.'''

def height(root):
    if root==None:
        return -1
    
    lheight=height(root.left)
    rheight=height(root.right)
    
    return max(lheight,rheight)+1
