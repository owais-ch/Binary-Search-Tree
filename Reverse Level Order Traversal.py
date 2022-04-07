'''

Given the root of a binary tree, return the reverse level order traversal of its nodes' values. The solution should consider the binary tree nodes level by level in bottom-up order from left to right, i.e., process all nodes of the last level first, followed by all nodes of the second last level, and so on.

Input:
		   1
		 /   \
		/	  \
	   2	   3
	  /		  / \
	 /	  	 /	 \
	4		5	  6
		   / \
		  /   \
		 7	   8

Output: [7, 8, 4, 5, 6, 2, 3, 1]

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

	def findReverseLevelOrderTraversal(self, root: Node) -> List[int]:
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
				list1.append(root.data)
			else:
				traversal(root.left,level-1)
				traversal(root.right,level-1)
				
		tall=height(root)
		
		list1=[]
		
		for i in range(tall-1,-1,-1):
			traversal(root,i)
			
		return list1
