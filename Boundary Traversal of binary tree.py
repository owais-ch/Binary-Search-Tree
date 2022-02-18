'''Given a Binary Tree, find its Boundary Traversal.
The traversal should be in the following order: 

Left boundary nodes: defined as the path from the root to the left-most node ie- the leaf node you could reach when you always travel preferring the left subtree
over the right subtree. 
Leaf nodes: All the leaf nodes except for the ones that are part of left or right boundary.
Reverse right boundary nodes: defined as the path from the right-most node to the root. The right-most node is the leaf node you could reach when you always travel 
preferring the right subtree over the left subtree. Exclude the root from this as it was already included in the traversal of left boundary nodes.
Note: If the root doesn't have a left subtree or right subtree, then the root itself is the left or right boundary. '''

class Solution:
    def printBoundaryView(self, root):
        if root.left==None and root.right==None:
            return [root.data]
        current=root.left
        list1=[root.data]
        if current!=None:
            list1.append(current.data)
        while current!=None:
            
            if current.left:
                current=current.left
                list1.append(current.data) 
            elif current.right:
                current=current.right
                list1.append(current.data) 
            else:
                current=None
        if len(list1)>1:
            list1=list1[:len(list1)-1]   
        
        current=root.right
        list2=[]
        if current!=None:
            list2=[current.data]
        while current!=None:
            
            if current.right:
                current=current.right
                list2.append(current.data) 
            elif current.left:
                current=current.left
                list2.append(current.data) 
            else:
                current=None
                
        def traversal(root):
            if root==None:
                return None
            
            if root.left:
                traversal(root.left)
                
            if root.left==None and root.right==None:
                list1.append(root.data)
                
            if root.right:
                traversal(root.right)
        traversal(root)   
        
        if list2==[]:
            return list1
        
        return list1+list2[:len(list2)-1][::-1]
