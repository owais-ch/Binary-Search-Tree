'''Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:

Input: p = [1,2,3], q = [1,2,3]
Output: true'''

class Solution:
    def __init__(self):
        self.tail=True
    def isSameTree(self, p, q) -> bool:
        def traversal(p,q):
            if p==None and q==None:
                return  
            elif p==None and q!=None or p!=None and q==None:
                self.tail=False
                return
            elif p.val!=q.val:
                self.tail=False
                return
            elif p.left and q.left==None or p.left==None and q.left:
                self.tail=False
                return 
            elif p.right and q.right==None or p.right==None and q.right:
                self.tail=False
                return
            
        
            traversal(p.left,q.left)
            
            traversal(p.right,q.right)
            
            
        traversal(p,q)
        
        return self.tail
            
