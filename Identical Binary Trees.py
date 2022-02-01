'''Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem

Example :

Input : 

   1       1
  / \     / \
 2   3   2   3

Output : 
  1 or True'''

class Solution:
	def __init__(self):
        self.list1=[]
        self.list2=[]
	def isSameTree(self, A, B):
        def traversal(root,list1):
            if root==None:
                return None
            if root.left:
                traversal(root.left,list1)

            list1.append(root.val)

            if root.right:
                traversal(root.right,list1)

        traversal(A,self.list1)
        traversal(B,self.list2)

        if self.list1==self.list2:
            return 1

        return 0
