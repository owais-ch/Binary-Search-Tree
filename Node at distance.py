'''
Given a Binary Tree and a positive integer k. The task is to count all distinct nodes that are distance k from a leaf node. A node is at
k distance from a leaf if it is present k levels above the leaf and also, is a direct ancestor of this leaf node. If k is more than the height of Binary Tree,
then nothing should be counted.

Example 1:

Input:
        1
      /   \
     2     3
   /  \   /  \
  4   5  6    7
          \ 
          8
K = 2
Output: 2
'''
def printKDistantfromLeaf(root, k):
    def traversal2(root):
        nonlocal countz
        
        if root==None:
            return None
            
        countz+=1
        
        root.data=(root.data,countz)
        
        if root.left:
            traversal2(root.left)
            
        if root.right:
            traversal2(root.right)
            
    countz=0
    temp=root.data 
    traversal2(root)
     
     
    def traversal(root):
        
        if root==None:
            return None
            
           
        if root.left:
            dict1[root.left.data]=root.data
            if root.left.left==None and root.left.right==None:
                list1.append(root.left.data)
            
        if root.right:
            dict1[root.right.data]=root.data
            if root.right.left==None and root.right.right==None:
                list1.append(root.right.data)
        
        if root.left:
            traversal(root.left)
            
        if root.right:
            traversal(root.right)
    
    list1=[]
    dict1=dict()
    
    traversal(root)
    
    
    dict1[(temp,1)]=(-1,-1)
    
    list3=[]
    
    dict2=dict()
    
    for i in list1:
        count=0
        node=i
        
        while count<k and node!=(-1,-1):
            node=dict1[node]
            count+=1
        
        if node not in dict2 and node!=(-1,-1):
            dict2[node]=1
    
    return len(dict2)
