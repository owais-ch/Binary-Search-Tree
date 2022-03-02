'''

Given the root of a binary search tree (BST) and a tree node x, find the floor and ceiling of node x in the BST. If node x lies in the BST, then both floor and ceil are equal to that node; otherwise, the ceil is equal to the next greater node (if any) in the BST, and the floor is equal to the previous greater node (if any) in the BST.

The solution should return the (floor, ceil) pair. If the floor or ceil doesn't exist, consider it to be None.

For example, consider the following BST.

		  8
		/	\
	   /	 \
	  /		  \
	 4		  10
	/ \		 /  \
   /   \	/	 \
  2		6  9	 12

Input: Node 7
Output: (Node 6, Node 8)
Explanation: The floor of node 7 is node 6, and ceil is node 8.

Input: Node 9
Output: (Node 9, Node 9)
Explanation: Node 9 lies in the BST. Hence both floor and ceil are equal to node 9.

Input: Node 1
Output: (None, Node 2)
Explanation: The floor of node 1 doesn't exist and ceil is node 2.

Input: Node 15
Output: (Node 12, None)
Explanation: The floor of node 15 is node 12 and its ceil doesn't exist.

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

	def findFloorAndCeil(self, root: Node, x: Node) -> Tuple[Node]:
		def traversal(root):
			if root==None:
				return None
			
			list1.append(root)
			
			if root.left:
				traversal(root.left)
				
			if root.right:
				traversal(root.right)
				
		list1=[]
		
		traversal(root)
		if list1==[]:
			return (None,None)
		list1.sort(key=lambda x:x.data)
		if x in list1:
			return (x,x)
		else:
			if list1[0].data>x.data:
				return (None,list1[0])
				
				
			for i in range(1,len(list1)):
				if list1[i-1].data<x.data and list1[i].data>x.data:
					return (list1[i-1],list1[i])
					
			if list1[-1].data<x.data:
				return (list1[-1],None)
