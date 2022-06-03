'''

Given the root of a perfect binary tree, return the values of alternating left and right nodes for each level.

Input:
					1
				  /	   \
			   /		 \
			/			   \
		  2					 3
		/   \				/  \
	  /		  \			  /		 \
	 4		   5		 6		  7
	/ \		  / \		/ \		 / \
   /   \	 /   \	   /   \	/   \
  8		9   10   11   12   13  14   15

Output: [1, 2, 3, 4, 7, 5, 6, 8, 15, 9, 14, 10, 13, 11, 12]

'''

class Solution:
	def traverse(self, root: Node) -> List[int]:
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
			
			list2=[]		
			for k in dict1.values():
				length=len(k)
				
				i,j=0,length-1
				
				while i<j:
					list2.extend([k[i],k[j]])
					i+=1
					j-=1
				if length%2!=0:
					list2.append(k[i])
			return list2
				
		return traversal(root)		
