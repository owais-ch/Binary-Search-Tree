'''Given a Binary Tree of size N , You have to count leaves in it. For example, there are two leaves in following tree

Input:
Given Tree is 
               4
             /   \
            8     10
           /     /   \
          7     5     1
         /
        3 
Output:
3
Explanation: 
Three leaves are 3 , 5 and 1.'''

def countLeaves(root):
    def traversal(root):
        nonlocal count
        if root==None:
            return None
            
        if root.left==None and root.right==None:
            count+=1
        
        if root.left:
            traversal(root.left)
            
        if root.right:
            traversal(root.right)
            
    
    count=0
    
    traversal(root)
    
    return count
