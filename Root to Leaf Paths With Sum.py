'''Given a binary tree and a sum, find all root-to-leaf paths where each path’s sum equals the given sum.

For example:

Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return

[
   [5,4,11,2],
   [5,8,4,5]
]'''

class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @return a list of list of integers
	def pathSum(self, root, sum1):
        def traversal(root):
            if root==None:
                return None
            
            stack.append(root.val)

            if root.left:
                traversal(root.left)

            if root.left==None and root.right==None:
                if sum(stack)==sum1:
                    list1.append(stack.copy())

            if root.right:
                traversal(root.right)

            stack.pop()

        list1=[]
        stack=[]

        traversal(root)

        return list1
