'''Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

Example 1:

Input: root = [4,2,6,1,3]
Output: 1'''

class Solution:
    def __init__(self):
        self.list1=[]
    def getMinimumDifference(self, root):
        
        def traversal(root):
            if root.left:
                traversal(root.left)
                
            self.list1.append(root.val) 
            
            if root.right:
                traversal(root.right)
                
        traversal(root)
        length=len(self.list1)
        
        minimum=9999999

        for i in range(length-1):
            if abs(self.list1[i]-self.list1[i+1])<minimum:
                minimum=abs(self.list1[i]-self.list1[i+1])
            
        return minimum
