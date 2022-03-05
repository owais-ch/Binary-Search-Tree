'''

Given the root of a binary search tree (BST) and a target, return a triplet of nodes in the BST such that their sum is equal to the target. The solution can return triplet in any order.

Input: target = 20

		  10
		/	 \
	   /	  \
	  /		   \
	-15		   20
	/  \	  /  \
   /	\	 /	  \
 -40	 3  15	  50

Output: (Node -40, Node 10, Node 50)


Input: target = 5

	 2
	/ \
   /   \
  1		3

Output: ()


Each input can have multiple solutions. The output should match with either one of them.

Input: target = 10

		  5
		/	\
	   /	 \
	  /		  \
	 2		   7
	/ \		  / \
   /   \	 /	 \
  1		3   8	  9

Output: (Node 2, Node 5, Node 3) or (Node 7, Node 2, Node 1)

'''

class Solution:
	def findTriplet(self, root: Node, target: int) -> Tuple[Node]:
		def traversal(root):
			if root==None:
				return None
				
			if root.left:
				traversal(root.left)
				
			list1.append(root)	
			list2.append(root.data)
			if root.right:
				traversal(root.right)
				
		list1=[]
		list2=[]
		traversal(root)
		
		length=len(list1)
		
		for i in range(length-1):
			for j in range(i+1,length):
				number=list2[i]+list2[j]
				number2=target-number
				if number2 in list2 and number2!=list2[i] and number2!=list2[j]:
					index1=list2.index(number2)
					
					return (list1[i],list1[j],list1[index1])
					
		return ()
