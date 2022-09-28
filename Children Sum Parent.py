
'''
Given a Binary Tree. Check whether all of its nodes have the value equal to the sum of their child nodes.


Example 1:

Input:
     10
    /
  10 
Output: 1
Explanation: Here, every node is sum of
its left and right child.

'''

#####  note: use postorder traversal

class Solution:
    def __init__(self):
        self.f=1
    def isSumProperty(self, root):
        def traversal(root):
            if root==None:
                return None
                
            if root.left:
                traversal(root.left)
            if root.right:
                traversal(root.right)
                
            if root.left and root.right:
                if root.left.data+root.right.data!=root.data:
                    self.f=0
                    return 
            elif root.left and root.right==None:
                if root.left.data!=root.data:
                    self.f=0
                    return 
            elif root.left==None and root.right:
                if root.right.data!=root.data:
                    self.f=0
                    return 
        traversal(root)
        return self.f

