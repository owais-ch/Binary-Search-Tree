'''Given a Binary Tree of size N, Print the corner nodes ie- the node at the leftmost and rightmost of each level.


Example 1:

Input :
         1
       /  \
     2      3
    / \    / \
   4   5  6   7    
Output: 1 2 3 4 7
Explanation:
Corners at level 0: 1
Corners at level 1: 2 3
Corners at level 2: 4 7'''

from collections import deque
def printCorner(root):
    def traversal(root):
        q=deque([])
        q.append(root)
        list2=[]
        list1=[]
        while len(q)>0:
            count=len(q)
            while count>0:
                temp=q.popleft()
                
                list1.append(temp.data)
                
                if temp.left:
                    q.append(temp.left)
                    
                if temp.right:
                    q.append(temp.right)
                    
                count-=1
                
            if len(list1)==1:
                list2.append(list1[0])
            else:
                list2.append(list1[0])
                list2.append(list1[-1])
                
            list1=[]
        for i in list2:
            print(i,end=' ')    

        
    traversal(root)
