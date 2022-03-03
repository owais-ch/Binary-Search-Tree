'''

Given the root of two binary search trees, merge them into a doubly-linked list in sorted order.

Input: Below BSTs

	  20
	 /  \
   10	30
		/  \
	   25  100

	  50
	 /  \
	5	70

Output: 5 ⇔ 10 ⇔ 20 ⇔ 25 ⇔ 30 ⇔ 50 ⇔ 70 ⇔ 100

The solution should return the head of the doubly-linked list constructed from the tree nodes.

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

	def mergeBSTs(self, x: Node, y: Node) -> Node:
		def traversal(root):
			if root==None:
				return None
			
			list1.append(root)
			
			if root.left:
				traversal(root.left)
				
			if root.right:
				traversal(root.right)
				
		list1=[]
		
		traversal(x)
		traversal(y)
		list1.sort(key=lambda x:x.data)
		length=len(list1)
		
		if list1==[]:
			return None
		
		m=list1[0]
		head=m
		
		for i in range(1,length):
			hh=list1[i]
			
			m.right=hh
			hh.left=m
			m=m.right
			
		m.right=None
		
		return head
