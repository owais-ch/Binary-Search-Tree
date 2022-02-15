'''You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.

For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.

The test cases are generated so that the answer fits in a 32-bits integer.

 

Example 1:


Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22'''


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def height(root):
            if root==None:
                return 0
            
            left=height(root.left)
            right=height(root.right)
            
            return max(left,right)+1
        
        def traversal(root,level,list1):
            if root==None:
                return None
            
            if level==0:
                list1.append(root)
            else:
                traversal(root.left,level-1,list1)
                traversal(root.right,level-1,list1)
                
        def traversal2(root,level,list2):
            if root==None:
                return None
            
            if level==0:
                if root.left==None and root.right==None:
                    list2.append(root)
            else:
                traversal2(root.left,level-1,list2)
                traversal2(root.right,level-1,list2)
                
                
        tall=height(root)
        
        if tall==1:
            return root.val
        
        list1=[]
        list2=[]
        
        for i in range(tall-1,-1,-1):
            traversal(root.left,i,list1)
            traversal2(root.left,i,list2)
            
        list1.append(root)
        
        length=len(list1)
        
        list4=[]
        for i in range(1,length):
            if list1[i-1] in list2:
                compare=list1[i-1]
                list3=[compare.val]
                for j in range(i,length):
                    if list1[j].left==compare or list1[j].right==compare:
                        compare=list1[j]
                        list3.append(compare.val)
                        
                list4.append(list3[::-1])
                
        list1=[]
        list2=[]
        
        for i in range(tall-1,-1,-1):
            traversal(root.right,i,list1)
            traversal2(root.right,i,list2)
            
        list1.append(root)
        
        length=len(list1)
        
        
        for i in range(1,length):
            if list1[i-1] in list2:
                compare=list1[i-1]
                list3=[compare.val]
                for j in range(i,length):
                    if list1[j].left==compare or list1[j].right==compare:
                        compare=list1[j]
                        list3.append(compare.val)
                        
                list4.append(list3[::-1]) 
                
        return sum(list(map(lambda x:int(x,2),[''.join(list(map(str,x))) for x in list4])))
