'''Problem Statement
You are given an arbitrary binary tree. A binary tree is called special if every node of this tree has either zero or two children. You have to determine if the given binary tree is special or not.
If the given binary tree is special, return True. Else, return False to the given function.'''

def isSpecialBinaryTree(root):
    def traversal(root):
        nonlocal count
        if root==None:
            return None
        
        if (root.left==None and root.right!=None) or (root.left!=None and root.right==None):
            count=False
            return 
        
        if root.left:
            traversal(root.left)
        if root.right:
            traversal(root.right)
            
    count=True
    traversal(root)
    return count
