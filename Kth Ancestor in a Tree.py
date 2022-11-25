'''Given a binary tree of size  N, a node, and a positive integer k., Your task is to complete the function kthAncestor(), the function should 
return the kth ancestor of the given node in the binary tree. If there does not exist any such ancestor then return -1.
Note: It is guaranteed that the node exists in the tree.


Example 1:



Input:
     K = 2
     Node = 4
Output: 1
'''

def kthAncestor(root,k, node):
    def parent(root):
        if root==None:
            return None
            
        if root.left:
            dict1[root.left.data]=root.data
        if root.right:
            dict1[root.right.data]=root.data
            
        if root.left:
            parent(root.left)
            
        if root.right:
            parent(root.right)
            
    dict1=dict()
    
    parent(root)
    
    node1=node
    if node==root.data:
        return -1
    
    count=k
    
    while count>0 and node1!=root.data:
        node1=dict1[node1]
        count-=1
    if count>0:
        return -1
    return node1
