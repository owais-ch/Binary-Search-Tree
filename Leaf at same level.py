'''Given a Binary Tree, check if all leaves are at same level or not.

Example 1:

Input: 
            1
          /   \
         2     3

Output: 1

Explanation: 
Leaves 2 and 3 are at same level.'''

class Solution:
    def __init__(self):
        self.dict1=dict()
    def check(self, root):
        def traversal(root):
            if root==None:
                return None
                
            q=deque([])
            q.append(root)
            output=0
            while len(q)>0:
                count=len(q)
                output+=1
                while count>0:
                    temp=q.popleft()
                    
                    if temp.left==None and temp.right==None:
                        self.dict1[output]=1
                        
                    if temp.left:
                        q.append(temp.left)
                        
                    if temp.right:
                        q.append(temp.right)
                        
                    count-=1
                    
                if len(self.dict1.keys())>1:
                    return False
                    
            return True
                
        return traversal(root)  
