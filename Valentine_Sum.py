'''
Valentine Sum (GFG)
Cupid wants to strike maximum houses in Geek Land on Valentine's Day. The houses in Geek Land are arranged in the form of a binary tree. 
Cupid is standing at target node initially. 
Find the sum of all nodes within a maximum distance k from target node. The target node should be included in the sum.

Input:
                   1
                 /    \
                2      9
               /      /  \
              4      5     7
            /   \         /  \
           8     19     20    11
          /     /  \
         30   40   50
target = 9, K = 1
Output:
22
Explanation:
Nodes within distance 1 from 9 are 9, 5, 7, 1  
'''
class Solution:
    def sum_at_distK(self, root, target, k):
        def parent(root):
            nonlocal num_nodes,node
            if root==None:
                return None
            
            num_nodes+=1  
            if root.data==target:
                node=root
                
            if root.left:
                dict_parent[root.left]=root
                parent(root.left)
                
            if root.right:
                dict_parent[root.right]=root
                parent(root.right)
                
        dict_parent=dict()
        num_nodes=0
        node=None
        
        parent(root)
        
        dict_parent[root]=None
        
        w=node
        visited={}
        distance={w:0}
        
        list1=[]
        count_visit=0
        
        while len(visited)<num_nodes:
            if count_visit==0:
                list1.append(w)
                count_visit+=1
            else:
                w=list1.pop(0)
                
                if w not in visited:
                    if w.left and w.left not in distance:
                            distance[w.left]=distance[w]+1
                            list1.append(w.left)
                            
                    if w.right and w.right not in distance:
                        distance[w.right]=distance[w]+1
                        list1.append(w.right)
                        
                    if dict_parent[w]!=None and dict_parent[w] not in distance:
                        distance[dict_parent[w]]=distance[w]+1
                        list1.append(dict_parent[w])
                    
                visited[w]=1
                    
        sum_total=0
        
        for i in distance:
            if distance[i]<=k:
                sum_total+=i.data
        
        return sum_total
