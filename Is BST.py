'''

Given the root of a binary tree, check if it is a binary search tree (BST) or not.

Input:
		  15
		/	 \
	   /	  \
	  /		   \
	 10		   20
	/  \	  /  \
   /	\	 /	  \
  8		12	16	  25

Output: True

Input:
		   1
		 /   \
		/	  \
	   2	   3

Output: False

'''

class Solution:

	'''
	A binary tree node is defined as:

	class Node:
		def __init__(self, data=None, left=None, right=None):
			self.data = data	# data field
			self.left = left	# pointer to the left child
			self.right = right	# pointer to the right child
	'''

	def isBST(self, root: Node) -> bool:
		def traversal(root):
			if root==None:
				return None
			
			if root.left:
				traversal(root.left)
				
			list1.append(root.data)	
			
			if root.right:
				traversal(root.right)
				
		list1=[]
		
		traversal(root)
		
		if list1==sorted(list1):
			return True
			
		return False
