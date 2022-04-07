'''

Given the root of a binary tree, return the spiral level order traversal of its nodes' values. The solution should consider the binary tree nodes level by level in spiral order, i.e., all nodes present at level 1 should be processed first from left to right, followed by nodes of level 2 from right to left, followed by nodes of level 3 from left to right and so on… In other words, odd levels should be processed from left to right, and even levels should be processed from right to left.

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

Output: [1, 3, 2, 4, 5, 6, 8, 7]

'''

class Solution:
	def findSpiralOrderTraversal(self, root: Node) -> List[int]:
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
				
		list1=[]
		list2=[]
		
		tall=height(root)
		
		for i in range(tall):
			traversal(root,i)
			if i%2==0:
				list2.extend(list1)
			else:
				list2.extend(list1[::-1])
				
				
			list1=[]
			
		return list2
