'''

Given the root of two binary trees, check whether the leaf traversals of both trees are the same or not.

Input:
		   1						1
		 /   \					  /   \
		/	  \					 /	   \
	   2	   3				2		3
	  /	\	  /					 \	   / \
	 /	 \ 	 /				  	  \	  /	  \
	4	  5	6				 	   4 5	   6

Output: True
Explanation: The leaf traversal of both binary trees is [4, 5, 6].

Input:
		   1						1
		 /   \					  /   \
		/	  \					 /	   \
	   2	   3				2		3
	  /	\					   		   / \
	 /	 \			  				  /	  \
	4	  5							 4	   5

Output: False
Explanation: Both binary trees have different leaf traversals.

'''

class Solution:
	def isLeafTraversalSame(self, x: Node, y: Node) -> bool:
		def traversal(root,list1):
			if root==None:
				return None
			
			if root.left==None and root.right==None:
				list1.append(root.data)
				
			if root.left:
				traversal(root.left,list1)
			if root.right:
				traversal(root.right,list1)
		
		list1=[]
		list2=[]
		
		traversal(x,list1)
		traversal(y,list2)
		
		if list1==list2:
			return True
		return False
