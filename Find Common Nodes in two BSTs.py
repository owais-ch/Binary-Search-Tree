'''Given two Binary Search Trees. Find the nodes that are common in both of them, ie- find the intersection of the two BSTs.

Example 1:

Input:
BST1:
                  5
               /     \
             1        10
           /   \      /
          0     4    7
                      \
                       9
BST2:
                10 
              /    \
             7     20
           /   \ 
          4     9
Output: 4 7 9 10'''

class Solution:
    
    def __init__(self):
        self.list1=[]
        self.list2=[]
    def findCommon(self, root1, root2):
        def traversal(root,list1):
            if root.left:
                traversal(root.left,list1)
                
            list1.append(root.data)
            
            if root.right:
                traversal(root.right,list1)
                
        traversal(root1,self.list1)
        traversal(root2,self.list2)
        
        list2=sorted(list(set(self.list1).intersection(set(self.list2))))
        
        return list2
