'''Given a binary tree containing n nodes. The problem is to find the sum of all the parent node’s which have a child node with value x.

Examples: 

Play Video
Input : Binary tree with x = 2:
        4        
       / \       
      2   5      
     / \ / \     
    7  2 2  3    
Output : 11

        4        
       / \       
      2   5      
     / \ / \     
    7  2 2  3    

The highlighted nodes (4, 2, 5) above
are the nodes having 2 as a child node.'''

def parent_nodex(root,x):
    def traversal(root):
        nonlocal total
        if root==None:
            return 0

        if root.left:
            if root.left.data==x:
                print('root1.data=',root.data)
                total+=root.data
        if root.right:
            if root.right.data==x:
                total+=root.data

        if root.left:
            traversal(root.left)
            
        if root.right:
            traversal(root.right)
            
    total=0
    traversal(root)
    
    return total
