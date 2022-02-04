'''Given a Binary Tree, print Left view of it. Left view of a Binary Tree is set of nodes visible when tree is visited from Left side. The task is to complete the function leftView(), 
which accepts root of the tree as argument.'''

def LeftView(root):
    def traversal(root,level):
        if root==None:
            return
        if len(list1)==level:
            list1.append(root.data)
            
        if root.left:
            traversal(root.left,level+1)
            
        if root.right:
            traversal(root.right,level+1)
    list1=[]        
    traversal(root,0)
    
    return list1
