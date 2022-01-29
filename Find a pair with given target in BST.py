'''Given a Binary Search Tree and a target sum. Check whether there's a pair of Nodes in the BST with value summing up to the target sum. 

Example 1:

Input:
        2
      /   \
     1     3
sum = 5
Output: 1 
Explanation: 
Nodes with value 2 and 3 sum up to 5.'''

class Solution:
    def __init__(self):
        self.list1=[]
    def isPairPresent(self,root, target):
        def traversal(root):
            if root.left:
                traversal(root.left)
                
            self.list1.append(root.data)
            
            if root.right:
                traversal(root.right)
                
        traversal(root)
        
        length=len(self.list1)
        
        i=0;j=length-1
        
        while i<j:
            if self.list1[i]+self.list1[j]<target:
                i+=1
            elif self.list1[i]+self.list1[j]>target:
                j-=1
            else:
                return 1
                
        return 0
