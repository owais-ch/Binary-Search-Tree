'''Given below is a binary tree. The task is to print the top view of binary tree. Top view of a binary tree is the set of nodes visible when the tree is viewed from the top.
For the given below tree

       1
    /     \
   2       3
  /  \    /   \
4    5  6   7

Top view will be: 4 2 1 3 7
Note: Return nodes from leftmost node to rightmost node.

Example 1:

Input:
      1
   /    \
  2      3
Output: 2 1 3'''

from collections import OrderedDict
class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        def traversal(root):
            if root==None:
                return None
                
            q=deque()
            q.append(root)
            hd=0
            dict1={root:hd}
            list1=[]
            while len(q)>0:
                count=len(q)
                while count>0:
                    temp=q.popleft()
                    
                    list1.append([dict1[temp],temp.data])
                    
                    if temp.left:
                        q.append(temp.left)
                        dict1[temp.left]=dict1[temp]-1
                        
                    if temp.right:
                        q.append(temp.right)
                        dict1[temp.right]=dict1[temp]+1
                        
                    count-=1
                    
            list1.sort(key=lambda x:x[0])
            
            dict2=OrderedDict()
            
            for i in list1:
                if i[0] not in dict2:
                    dict2[i[0]]=[i[1]]
                else:
                    dict2[i[0]].append(i[1])
            #print(dict2)        
            list3=[]
            
            for i in dict2:
                list3.append(dict2[i][0])
                
            return list3
            
        return traversal(root)
