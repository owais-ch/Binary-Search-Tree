'''Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and
alternate between).

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]'''

from collections import deque

class Solution:
    def __init__(self):
        self.list1=[]
    def zigzagLevelOrder(self, root) -> List[List[int]]:
        def traversal(root):
            if root==None:
                return []
            q=deque([])
            q.append(root)
            list2=[]
            level=0
            while len(q)>0:
                count=len(q)
                
                while count>0:
                    temp=q.popleft()
                    
                    self.list1.append(temp.val)
                    
                    if temp.left:
                        q.append(temp.left)
                        
                    if temp.right:
                        q.append(temp.right)
                        
                    count-=1
                if level%2==0:    
                    list2.append(self.list1)
                else:
                    list2.append(self.list1[::-1])
                self.list1=[]
                level+=1
                
            return list2
        
        return traversal(root)

