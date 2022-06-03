'''

Given the root of a binary tree and two positive numbers m and n where m >= n, return values of all nodes between level m and level n. The nodes for each level should be processed from left and right.

Input: Below binary tree, m = 2, n = 3

		   1
		 /   \
		/	  \
	   2	   3
			  / \
			 /	 \
			4	  5
		   / \	   \
		  /   \		\
		 6	   7	 8

Output: [2, 3, 4, 5]

Note: If n is more than the number of levels in the binary tree, the solution return nodes till last level. For example, if the starting level is 2 and the ending level is 7, the solution should return [2, 3, 4, 5, 6, 7, 8] for above binary tree.

'''

class Solution:
	def findNodes(self, root: Node, m: int, n: int) -> List[int]:
		def traversal(root):
			if root==None:
				return []
				
			hd=1
			
			q=[[root,hd]]
			
			dict1=dict()
			list2=[]
			
			
			while q!=[]:
				node=q.pop(0)
				
				if node[1]>=m and node[1]<=n:
					list2.append(node[0].data)
				
				if node[1] not in dict1:
					dict1[node[1]]=[node[0].data]
				else:
					dict1[node[1]].append(node[0].data)
					
				hd=node[1]
				
				if node[0].left:
					q.append([node[0].left,hd+1])
				if node[0].right:
					q.append([node[0].right,hd+1])
				
			return list2
		return traversal(root)
