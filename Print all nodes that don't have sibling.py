'''Given a Binary Tree of size N, find all the nodes which don't have any sibling. You need to return a list of integers containing all the nodes that don't have a sibling in sorted order.

Note: Root node can not have a sibling so it cannot be included in our answer.

Example 1:

Input :
       37
      /   
    20
    /     
  113 

Output: 20 113'''


def noSibling(root):
    def traversal(root):
        if root==None:
            return None
        
        if root.left and root.right==None:
            list1.append(root.left.data)
        if root.right and root.left==None:
            list1.append(root.right.data)    
        if root.left:
            traversal(root.left)
        
        if root.right:
            traversal(root.right)
            
        
            
    list1=[]
    
    traversal(root)
    if list1==[]:
        return [-1]
    return sorted(list1)
