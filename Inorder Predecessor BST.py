'''

Given the root of a binary search tree (BST) and a tree node x, find the inorder predecessor of x in the BST. An inorder predecessor of a tree node is the previous node in the inorder traversal of the tree.

For example, consider the following tree:

		  15
		/	 \
	   /	  \
	  /		   \
	 10		   20
	/  \	  /  \
   /	\	 /	  \
  8		12	16	  25

Input: Node 10
Output: Node 8

Input: Node 12
Output: Node 10

• If the node does not lie in the BST, return the previous greater node (if any) present in the BST.

Input: Node 18
Output: Node 16

• If the node does not lie in the BST and the previous greater node also does not exist, the solution should return None.

Input: Node 8
Output: None

'''

class Solution:
	def findInorderPredecessor(self, root: Node, x: Node) -> Node:
		def traversal(root):
			if root==None:
				return None
				
			if root.left:
				traversal(root.left)
				
			list1.append(root)
			
			if root.right:
				traversal(root.right)
				
		list1=[]
		
		traversal(root)
		if list1==[]:
			
			return None
		length=len(list1)
		
		if x in list1:
			index1=list1.index(x)
			if index1==0:
				return None
			return list1[index1-1]
		else:
			for i in range(length-1):
				if list1[i].data<x.data and list1[i+1].data>x.data:
					return list1[i]
					
		if list1[-1].data<x.data:
			return list1[-1]
		else:
			return None
