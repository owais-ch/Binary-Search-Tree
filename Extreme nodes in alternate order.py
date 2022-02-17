'''Given a binary tree, print nodes of extreme corners of each level but in alternate order.'''

class Solution:
    # Your task is to complete this function
    def ExtremeNodes(self, root):
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
                list1.append(root.data)
            else:
                traversal(root.left,level-1)
                traversal(root.right,level-1)
                
        tall=height(root)
        
        list1=[]
        list2=[]
        
        for i in range(tall):
            traversal(root,i)
            
            if i%2==0:
                list2.append(list1[-1])
            else:
                list2.append(list1[0])
                
            list1=[]
            
        return list2
