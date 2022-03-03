'''

Given the root of a binary search tree (BST) and a target, return a pair of nodes in the BST such that their sum is equal to the target. The solution can return pair in any order.

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
Output: (Node 8, Node 12)

• Each input can have multiple solutions. The output should match with either one of them.

Input: target = 14
Output: (Node 6, Node 8) or (Node 4, Node 10)

• If no pair with the given sum exists, the solution should return an empty tuple ().

Input: target = 25
Output: ()

'''

class Solution:
	def findPair(self, root: Node, target: int) -> Tuple[Node]:
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
		
		list2=[i.data for i in list1]
		
		length=len(list1)
		
		for i in range(length):
			number=target-list2[i]
			if number in list2 and number!=list2[i]:
				index1=list2.index(number)
				return (list1[i],list1[index1])
				
		return ()
