'''

Given the root of a binary search tree (BST) and an integer k, insert k into the BST. The solution should not rearrange the existing tree nodes and insert a new node with the given key at its correct position in BST.

Input: Below BST, k = 16

		  15
		/	 \
	   /	  \
	  /		   \
	 10		   20
	/  \		 \
   /	\	 	  \
  8		12		  25

Output:

		  15
		/	 \
	   /	  \
	  /		   \
	 10		   20
	/  \	  /  \
   /	\	 /	  \
  8		12	16	  25

You may assume that the key does not exist in the BST.

'''

class Solution:

	'''
	A BST node is defined as:

	class Node:
		def __init__(self, data=None, left=None, right=None):
			self.data = data	# data field
			self.left = left	# pointer to the left child
			self.right = right	# pointer to the right child
	'''

	def insert(self, root: Node, k: int) -> Node:
		if root==None:
			return Node(k)
			
		if root.data>k:
			if root.left:
				self.insert(root.left,k)
			else:
				root.left=Node(k)
		else:
			if root.right:
				self.insert(root.right,k)
			else:
				root.right=Node(k)
		return root
