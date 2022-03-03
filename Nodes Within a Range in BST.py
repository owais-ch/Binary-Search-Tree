'''

Given the root of a binary search tree (BST) and a range of BST keys, return the count of BST nodes that lie within a given range.

Input: Below BST, low = 12, high = 20

				15
			  /	   \
			/		 \
		  /			   \
		 10				 25
	   /	\		   /	\
	  /		 \		  /		 \
	 8		 12		 20		 30
	/ \				/  \
   /   \		   /	\
  6		9		  18	22

Output: 4
Explanation: The BST nodes in range [12, 20] are 12, 15, 18, and 20.

'''
class Solution:
	def countNodes(self, root: Node, low: int, high: int) -> int:
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
		
		count=0
		
		for i in range(length):
			if list1[i]>=low and list1[i]<=high:
				count+=1
				
		return count
