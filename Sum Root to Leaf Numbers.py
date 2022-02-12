'''You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

Example 1:

Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.'''


class Solution:
    def __init__(self):
        self.list1=[]
    def sumNumbers(self, root) -> int:
        def traversal(root):
            if root==None:
                return None
            elif root.left==None and root.right==None:
                self.list1.append(root)
                
            if root.left:
                traversal(root.left)
                
            if root.right:
                traversal(root.right)
                
        def height(root):
            if root==None:
                return 0
            
            left=height(root.left)
            right=height(root.right)
            
            return max(left,right)+1
        
        def traversal2(root,level):
            if root==None:
                return None
            
            if level==0:
                list2.append(root)
            else:
                traversal2(root.left,level-1)
                traversal2(root.right,level-1)
        if root.left==None and root.right==None:
            return root.val
        traversal(root)
        
        tall=height(root)
        list2=[]
        list3=[]
        for i in range(tall-1,-1,-1):
            traversal2(root,i)
            list3.extend(list2)
            list2=[]
            
        list5=[]    
        
        for i in range(1,len(list3)):
            if list3[i-1] in self.list1:
                compare=list3[i-1]
                
                list4=[compare.val]
                for j in range(i,len(list3)):
                    if list3[j].left==compare or list3[j].right==compare:
                        list4.append(list3[j].val)
                        compare=list3[j]
                
                
                list5.append(list4)
                list4=[]
                
        total=0
        
        for i in list5:
            string=''
            for j in i:
                string+=str(j)
                
            number=int(string[::-1])
            total+=number
            
        return total
