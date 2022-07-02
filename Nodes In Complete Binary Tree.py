'''Problem Statement
You are given the root of a complete binary tree, you need to calculate the number of nodes in the given complete binary tree.
A complete binary tree is a tree in which all the levels are completely filled except the last level. Nodes in the last level are as left as possible.'''

def countNodes(root):
    def traversal(root):
        nonlocal count
        if root==None:
            return 0
        
        count+=1
        
        if root.left:
            traversal(root.left)
        if root.right:
            traversal(root.right)
            
    count=0
    traversal(root)
    
    return count
