'''

Given the root of a binary search tree (BST) and a key, search for the node with that key in the BST.

For example, consider the following BST.

		  15
		/	 \
	   /	  \
	  /		   \
	 10		   20
	/  \	  /  \
   /	\	 /	  \
  8		12	16	  25

Input: key = 25
Output: True

Input: key = 5
Output: False

'''

class Solution:
	def search(self, root: Node, key: int) -> bool:
		def traversal(root):
			nonlocal output
			if root==None:
				return None
				
			if root.data==key:
				output=True
				return 
				
			if root.data>key:
				if root.left:
					traversal(root.left)
			elif root.data<key:
				if root.right:
					traversal(root.right)
		output=False			
		traversal(root)
		
		return output
