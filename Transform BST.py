'''

Given the root of a binary search tree (BST), in-place modify the BST such that every node is updated to contain the sum of all greater keys present in the BST.

Input:

		  5
		/	\
	   /	 \
	  /		  \
	 3		   8
	/ \		  / \
   /   \	 /	 \
  2		4   6	 10

Output:

		  29
		/	 \
	   /	  \
	  /		   \
	 36		   18
	/  \	  /  \
   /	\	 /	  \
  38	33	24	  10

'''

class Solution:
	def transform(self, root: Node) -> None:
		def traversal(root):
			nonlocal sum1
			if root==None:
				return None
				
			sum1+=root.data
			
			if root.left:
				traversal(root.left)
				
			if root.right:
				traversal(root.right)
				
		sum1=0
		
		traversal(root)
		
		def traversal2(root):
			nonlocal sum1
			if root==None:
				return None
				
			if root.left:
				traversal2(root.left)
			
			temp=root.data
			root.data=sum1
			sum1=sum1-temp
			
			if root.right:
				traversal2(root.right)
		
		traversal2(root)
		
		return root
