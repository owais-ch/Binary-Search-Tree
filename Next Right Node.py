'''Given a Binary tree and a key in the binary tree, find the node right to the given key. If there is no node on right side, then return a node with value -1.

Example 1:

Input:

       10
     /    \
    2      6
   / \      \
  8   4      5
and key = 2
Output: 6
Explanation: We can see in the above tree
that the next right node of 2 is 6.'''

class Solution:
    def nextRight(self, root, key):
        def traversal(root,level):
            nonlocal f
            if root==None:
                return None
                
            if root.data==key:
                f=level
                return 
            
            if root.left:
                traversal(root.left,level+1)
                
            if root.right:
                traversal(root.right,level+1)
                
        f=0
        
        traversal(root,0)
        
        def traversal2(root,level):
            if root==None:
                return None
                
            if level==0:
                list1.append(root)
            else:
                traversal2(root.left,level-1)
                traversal2(root.right,level-1)
                
        list1=[]
        
        traversal2(root,f)
        
        length=len(list1)
        
        for i in range(length):
            if list1[i].data==key and i+1<length:
                return list1[i+1]
                
        return Node(-1)
