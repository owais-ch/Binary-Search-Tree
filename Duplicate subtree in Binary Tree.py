'''
Given a binary tree, find out whether it contains a duplicate sub-tree of size two or more, or not.


Example 1 :

Input : 
               1
             /   \ 
           2       3
         /   \       \    
        4     5       2     
                     /  \    
                    4    5
Output : 1
Explanation : 
    2     
  /   \    
 4     5
is the duplicate sub-tree.
'''

class Solution:
    def dupSub(self, root):
        def isIdentical(root1,root2):
            if root1==None and root2==None:
                return True
            elif root1!=None and root2!=None and root1.data==root2.data:
                return isIdentical(root1.left,root2.left) and isIdentical(root1.right,root2.right)
            else:
                return False
                
        def traversal(root):
            nonlocal f
            if root==None:
                return None
                
            if root.left or root.right:
                if root.data not in dict1:
                    dict1[root.data]=[root]
                else:
                    for i in range(len(dict1[root.data])):
                        if isIdentical(root,dict1[root.data][i])==True:
                            f=1
                            
                    dict1[root.data].append(root)
            if root.left:
                traversal(root.left)
                
            if root.right:
                traversal(root.right)
                
        f=0
        dict1=dict()
        traversal(root)
        
        return f
