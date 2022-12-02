'''Given a BST, transform it into a greater sum tree where each node contains sum of all nodes greater than that node.'''

def convertBstToGreaterSum(root):
    def traversal(root):
        nonlocal temp
        if root==None:
            return None
        
        if root.right:
            traversal(root.right)
            
        temp+=root.val
        root.val=temp-root.val
        
        if root.left:
            traversal(root.left)
            
    temp=0
    
    traversal(root)
    
    return root
