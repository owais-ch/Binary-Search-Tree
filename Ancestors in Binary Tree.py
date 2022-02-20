'''Given a Binary Tree and a target key, you need to find all the ancestors of the given target key.

              1
            /   \
          2      3
        /  \
      4     5
     /
    7
Key: 7
Ancestor: 4 2 1'''

class Solution:
    def Ancestors(self, root,target):
        def traversal(root):
            nonlocal count,list1
            if root==None:
                return None
                
            stack.append(root.data)   
            
            if root.left:
                traversal(root.left)
                
            if target==stack[-1] and count==0:
                list1=stack.copy()
                count+=1
                return 
                
            if root.right:
                traversal(root.right)
                
            stack.pop()
            
        list1=0
        stack=[]
        count=0
        traversal(root)
        
        return list1[0:len(list1)-1][::-1]
