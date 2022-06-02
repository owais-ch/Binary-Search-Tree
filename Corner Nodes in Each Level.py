'''

Given the root of a binary tree, return corner nodes' values for each level in it.

Input:
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

Output: [1, 2, 3, 4, 5, 6, 8]

'''

class Solution:
	def findCornerNodes(self, root: Node) -> List[int]:
		def traversal(root):
			if root==None:
				return []
			
			hd=0
			q=[[root,hd]]
			dict1=dict()
			
			while q!=[]:
				node=q.pop(0)
				
				if node[1] not in dict1:
					dict1[node[1]]=[node[0].data]
				else:
					dict1[node[1]].append(node[0].data)
				
				hd=node[1]
				
				if node[0].left:
					q.append([node[0].left,hd+1])
				
				if node[0].right:
					q.append([node[0].right,hd+1])
					
			list1=[]
			
			for i in dict1:
				if len(dict1[i])==1:
					list1.append(dict1[i][0])
				elif len(dict1[i])>1:
					list1.extend([dict1[i][0],dict1[i][-1]])
					
			return list1
		
		return traversal(root)
