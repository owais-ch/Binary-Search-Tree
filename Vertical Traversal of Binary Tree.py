'''Given a Binary Tree, find the vertical traversal of it starting from the leftmost level to the rightmost level.
If there are multiple nodes passing through a vertical line, then they should be printed as they appear in level order traversal of the tree.

Input:
           1
         /   \
       2       3
     /   \   /   \
   4      5 6      7
              \      \
               8      9           
Output: 
4 2 1 5 6 3 8 7 9 '''

class Solution:
    
    def __init__(self):
        self.list1=[]
    def verticalOrder(self, root): 
        def traversal(root):
            if root==None:
                return None
            q=deque([])
            q.append(root)
            hd=0
            dict1={root:hd}
            list1=[]
            
            while len(q)>0:
                temp=q.popleft()
                
                list1.append([dict1[temp],temp.data])
                
                if temp.left:
                    q.append(temp.left)
                    dict1[temp.left]=dict1[temp]-1
                    
                if temp.right:
                    q.append(temp.right)
                    dict1[temp.right]=dict1[temp]+1
                    
            list1=sorted(list1,key=lambda x:x[0])  
            list1=list(map(lambda x:x[1],list1))
            return list1
        
        return traversal(root)
