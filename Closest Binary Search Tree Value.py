'''You are given a binary searvh tree with N nodes and target value k.Your task is to find the closest element with k in the given BST. If there are more than one such
element return the minimum amomg them'''

def findClosestElement(node, k):
    def traversal(root):
        nonlocal f,minimum
        if root==None:
            return None
        
        if root.left:
            traversal(root.left)
            
        if abs(root.data-k)<minimum:
            f=root.data
            minimum=abs(root.data-k)
        
        if root.right:
            traversal(root.right)
            
    minimum=999999
    f=-1
    
    traversal(node)
    
    return f
