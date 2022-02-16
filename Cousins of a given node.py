'''Given a binary tree and a node, print all cousins of given node in order of their appearance. Note that siblings should not be printed.

Example 1:

Input : 
             1
           /   \
          2     3
        /   \  /  \
       4    5  6   7

Given node : 5
Output : 6 7'''

class Solution:
    def __init__(self):
        self.list1=[]
    def printCousins(self, root, node_to_find):
        def traversal(root):
            if root==None:
                return None
                
            q=deque([])
            q.append(root)
            output=0
            while len(q)>0:
                count=len(q)
                while count>0:
                    temp=q.popleft()
                    if temp.left==node_to_find or temp.right==node_to_find:
                        output=1
                    else:
                        if temp.left:
                            self.list1.append(temp.left.data)
                        if temp.right:
                            self.list1.append(temp.right.data)
                            
                    if temp.left:
                        q.append(temp.left)
                    if temp.right:
                        q.append(temp.right)
                        
                    count-=1
                if output==1:
                    if self.list1!=[]:
                        return self.list1
                    else:
                        return [-1]
                output=0
                
                self.list1=[]
            
            return [-1]
        return traversal(root)
