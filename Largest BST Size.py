'''

Given the root of a binary tree, find the size of the largest binary search tree (BST) in the binary tree.

Input:
		   10
		 /	  \
		/	   \
	   15		8
	  /	 \	   / \
	 /	  \   /	  \
	12	  20 5	   2

Output: 3

Explanation: The largest BST in the binary tree is formed by a subtree rooted at node 15, having size 3:

	   15
	  /	 \
	 /	  \
	12	  20

'''

class Solution:
	def findLargestBSTSize(self, root: Node) -> int:
		def traversal(root):
			nonlocal count,maximum,list1
			if root==None:
				return None
				
			traversal2(root)
			
			
			length=len(list1)
			
			if list1==sorted(list1):
				count=length
			else:
				count=1
			
			maximum=max(maximum,count)	
			
			list1=[]
			count=1
			
			if root.left:
				traversal(root.left)
				
			if root.right:
				traversal(root.right)
				
		def traversal2(root):
			if root==None:
				return None
			
			if root.left:
				traversal2(root.left)
			
			list1.append(root.data)
			
			if root.right:
				traversal2(root.right)
		if root==None:
			return 0
		maximum=1		
		count=1
		list1=[]
		
		traversal(root)
		
		return maximum
