'''

Given the root of a binary search tree (BST) and two tree nodes, x and y, return the lowest common ancestor (LCA) of x and y in the BST.

The lowest common ancestor (LCA) of two nodes x and y in a BST is the lowest (i.e., deepest) node that has both x and y as descendants, where each node can be a descendant of itself (so if x is reachable from w, w is the LCA). In other words, the LCA of x and y is the shared ancestor of x and y that is located farthest from the root.

For example, consider the following BST.

				15
			  /   \
			/		\
		  /			  \
		 10			   25
	   /   \		 /   \
	  /		\		/	  \
	 8		12 	   20	  30
	/ \			  /  \
   /   \		 /	  \
  6		9		18	  22

Input: x = Node 6, y = Node 12
Output: Node 10
Explanation: The common ancestors of nodes 6 and 12 are 10 and 15. Out of nodes 10 and 15, the LCA is 10 as it is farthest from the root.

Input: x = Node 10, y = Node 12
Output: Node 10
Explanation: Node 12 itself is descendant of node 10 (and node 10 can be a descendant of itself).

Input: x = Node 20, y = Node 6
Output: Node 15

Input: x = Node 30, y = Node 30
Output: Node 30

Note: The solution should return None if either x or y is not the actual node in the tree.

'''

class Solution:
	def findLCA(self, root: Node, x: Node, y: Node) -> Node:
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
				list1.append(root)
			else:
				traversal(root.left,level-1)
				traversal(root.right,level-1)
		if x==y:
			return x
			
		tall=height(root)
		
		list1=[]
		
		for i in range(tall-1,-1,-1):
			traversal(root,i)
		if x not in list1 or y not in list1:
			return None
		length=len(list1)		
		
		output=0
		list2=[]
		list3=[]
		for i in range(length-1):
			compare=list1[i]
			
			if compare==x or compare==y:
				
				output+=1
				if output%2!=0:
					list2=[compare]
				else:
					list3=[compare]
				for j in range(i+1,length):
					if (list1[j].left==compare or list1[j].right==compare) and output%2!=0:
						compare=list1[j]
						list2.append(compare)
					elif (list1[j].left==compare or list1[j].right==compare) and output%2==0:
						compare=list1[j]
						list3.append(compare)
						
		
		if list2==[]:
			list2.append(root)
		if list3==[]:
			list3.append(root)
		
		print(list1,list2)
		for i in list2:
			if i in list3:
				return i
		for i in list3:
			if i in list2:
				return i
				
