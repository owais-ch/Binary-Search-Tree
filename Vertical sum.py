'''Given a Binary Tree, find vertical sum of the nodes that are in same vertical line. Print all sums through different vertical lines starting from left-most 
vertical line to right-most vertical line.

Example 1:

Input:
       1
    /   \
  2      3
 / \    / \
4   5  6   7'''

from collections import OrderedDict
class Solution:
    #Complete the function below
    def verticalSum(self, root):
        def traversal(root):
            if root==None:
                return None
                
            q=[]
            q.append(root)
            hd=0
            dict1={root:hd}
            list1=[]
            
            while len(q)>0:
                temp=q.pop(0)
                
                list1.append([dict1[temp],temp.data])
                
                
                if temp.left:
                    q.append(temp.left)
                    dict1[temp.left]=dict1[temp]-1
                    
                if temp.right:
                    q.append(temp.right)
                    dict1[temp.right]=dict1[temp]+1
                    
            list1=sorted(list1,key=lambda x:x[0])
            
            dict2=OrderedDict()
            
            for i in list1:
                if i[0] not in dict2:
                    dict2[i[0]]=[i[1]]
                else:
                    dict2[i[0]].append(i[1])
                 
            list3=[sum(dict2[i]) for i in dict2]
            
            return list3
        
        return traversal(root)
