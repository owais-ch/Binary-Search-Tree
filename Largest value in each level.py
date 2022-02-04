'''Given a binary tree, find the largest value in each level.

Example 1:

Input :
        1
       / \
      2   3 

Output : 1 3
Explanation : 
There are two levels in the tree :
1. {1}, max = 1
2. {2, 3}, max = 3'''


class Solution:
    def __init__(self):
        self.list1=[]
        self.list2=[]
        
    def largestValues(self, root):
        def height(root):
            if root==None:
                return 0
                
            left=height(root.left)
            right=height(root.right)
            
            return max(left,right)+1
            
        def level_order(root,level):
            if root==None:
                return None
            elif level==0:
                self.list1.append(root.data)
            else:
                level_order(root.left,level-1)
                level_order(root.right,level-1)
                
            return self.list1
            
        tall=height(root)
        start=0
        for i in range(tall):
            level_order(root,i)
            self.list2.append(max(self.list1[start:]))
            start=len(self.list1)
            
        return self.list2
