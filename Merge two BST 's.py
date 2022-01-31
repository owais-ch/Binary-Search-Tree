'''Given two BSTs, return elements of both BSTs in sorted form.

Example 1:

Input:
BST1:
       5
     /   \
    3     6
   / \
  2   4  
BST2:
        2
      /   \
     1     3
            \
             7
            /
           6
Output: 1 2 2 3 3 4 5 6 6 7'''


class Solution:
    
    def __init__(self):
        self.list1=[]
    def merge(self, root1, root2):
        def traversal(root):
            if root.left:
                traversal(root.left)
                
            self.list1.append(root.data)
            
            if root.right:
                traversal(root.right)
                
        traversal(root1)
        
        traversal(root2)
        
        self.list1.sort()
        
        return self.list1
