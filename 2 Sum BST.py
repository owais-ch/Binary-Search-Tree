'''

Given the root of a binary search tree (BST) and a target, check if there exists a pair of nodes in the BST with their sum equal to the target.

For example, consider the following BST.

		  8
		/	\
	   /	 \
	  /		  \
	 4		  10
	/ \		 /  \
   /   \	/	 \
  2		6  9	 12

Input: target = 20
Output: True
Explanation: Node 8 and 12 sums to target 20

Input: target = 14
Output: True
Explanation: Node 6 and 8 (or Node 4 and 10) sums to target 14

Input: target = 25
Output: False

'''

class Solution:
	def findPair(self, root: Node, target: int) -> bool:
		def traversal(root):
			if root==None:
				return None
				
			list1.append(root.data)
			
			if root.left:
				traversal(root.left)
				
			if root.right:
				traversal(root.right)
				
		list1=[]
		
		traversal(root)
		
		length=len(list1)
		
		for i in range(length):
			number=target-list1[i]
			if number in list1:
				if number!=list1[i]:
					return True
				elif list1.count(list1[i])>1:
					return True
					
		return False
