'''Given a binary tree and a budget. Assume you are at the root of the tree(level 1), you need to maximise the count of leaf nodes you can visit in your budget if
the cost of visiting a leaf node is equal to the level of that leaf node.

Example 1:

Input: 
                  10
                /    \
               8      2
             /      /   \
            3      3     6
                    \
                     4
and budget = 8
Output: 2
Explanation:
Cost For visiting Leaf Node 3: 3
Cost For visiting Leaf Node 4: 4
Cost For visiting Leaf Node 6: 3
In budget 8 one can visit Max 2 Leaf Nodes.'''

class Solution:
    def getCount(self,root,budget):
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
                if root.left==None and root.right==None:
                    list1.append(root.data)
            else:
                traversal(root.left,level-1)
                traversal(root.right,level-1)
                
        tall=height(root)
        
        list1=[]
        list2=[]
        
        for i in range(tall):
            traversal(root,i)
            if len(list1)>0:
                list2.extend([i+1]*len(list1))
                
            list1=[]
            
        list2.sort()
        length=len(list2)
        sum1=list2[0]
        i=1
        count=0
        while sum1<=budget and i<=length:
            count+=1
            if i>=length:
                return count
            sum1+=list2[i]
            i+=1
        
        return count
