'''Given two binary trees, the task is to find if both of them are identical or not. 

Example 2:

Input:
     1          1
   /   \      /   \
  2     3    2     3
Output: Yes
Explanation: There are two trees both having 3 nodes and 2 edges, both trees are identical having the root as 1, left child of 1 is 2 and right child of 1 is 3.'''

class Solution:
    def __init__(self):
        self.list1=[]
        self.list2=[]
    def isIdentical(self,root1, root2):
        def traversal(root,list1):
            if root==None:
                list1.append(None)
                
            list1.append(root.data)
            
            if root.left:
                traversal(root.left,list1)
                
            if root.right:
                traversal(root.right,list1)
                
        traversal(root1,self.list1)
        traversal(root2,self.list2)
        #print(self.list1,self.list2)
        if self.list1==self.list2:
            return 1
        return 0
