'''Given a Binary Tree, find the deepest leaf node that is left child of its parent. For example, consider the following tree. The deepest left leaf node 
is the node with value 9. 

       1
     /   \
    2     3
  /      /  \  
 4      5    6
        \     \
         7     8
        /       \
       9         10 
'''
node=-9999
maximum=-1
def deepest(root,level):
    global node,maximum
    if root==None:
        return None
    
    if root.left and root.left.left==None and root.left.right==None and level>maximum:
        maximum=level
        node=root.left.data
        
        
    if root.left:
        deepest(root.left,level+1)
        
    if root.right:
        deepest(root.right,level+1)
