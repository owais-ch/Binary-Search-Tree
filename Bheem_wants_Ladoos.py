'''
Bheem Wants Ladoos (GFG)

Chhota Bheem wants to eat the maximum number of ladoos in Dholakpur on Independence Day. The houses in Dholakpur are arranged in the form of a binary tree and have ladoos the same as their house number. Chhota Bheem is standing at his home initially. 
Find the maximum ladoos he can eat if he can go to houses within a maximum distance k from his house. The number of ladoos at his home should also be included in the sum.

Note: Every house has distinct ladoos in it. 
Example 1:

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
home = 9, K = 1
Output:
22
Explanation:
Initially Bheem at 9, so sum = 9
In 2nd move he went to 5, sum=9+5=14
In 3rd move he went to 7, sum=14+7=21
In 4th move he went to 1, sum=21+1=22
So within K distance bheem can get 22 ladoos.  
'''

class Solution:
    def ladoos(self, root, home, k):
        def parent(root):
            nonlocal node,num_nodes
            if root==None:
                return None
                
            if root.data==home:
                node=root
            num_nodes+=1
            
            if root.left:
                dict_parent[root.left]=root
                parent(root.left)
                
            if root.right:
                dict_parent[root.right]=root
                parent(root.right)
                
        dict_parent={root:None}
        node=None
        num_nodes=0
        
        parent(root)
        
        w=node
        distance={w:0}
        visited={}
        list1=[]
        countx=0
        
        while len(visited)<num_nodes:
            if countx==0:
                list1.append(w)
                countx+=1
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
                
