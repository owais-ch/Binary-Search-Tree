'''You are given the root of a complete binary tree A.

You have to return the value of the rightmost node in the last level of the binary tree.

A = 
    1
   / \
  2   3
Output:
3'''

class Solution:
    def __init__(self):
        self.list1=[]
    def lastNode(self, root):
        def height(root):
            if root==None:
                return 0

            left=height(root.left)
            right=height(root.right)

            return max(left,right)+1

        def traversal(root,level):
            if root==None:
                return None
            
            if level==0:
                self.list1.append(root.val)
            else:
                traversal(root.left,level-1)
                traversal(root.right,level-1)

        tall=height(root)

        traversal(root,tall-1)

        return self.list1[-1]
