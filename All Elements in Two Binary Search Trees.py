'''Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.

Example 1:

Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]'''

class Solution:
    def __init__(self):
        self.list1=[]
    def getAllElements(self, root1, root2):
        def traversal(root):
            if root==None:
                return
            if root.left:
                traversal(root.left)
                
            self.list1.append(root.val)
            
            if root.right:
                traversal(root.right)
                
        traversal(root1)
        traversal(root2)
        
        self.list1.sort()
        
        return self.list1
