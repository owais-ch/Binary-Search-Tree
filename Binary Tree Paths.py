'''Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

Example 1:
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]'''

class Solution:
    def __init__(self):
        self.list1=[]
        self.list2=[]
    def binaryTreePaths(self, root) -> List[str]:
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
                self.list1.append(root)
            else:
                traversal(root.left,level-1)
                traversal(root.right,level-1)
        def traversal2(root,level):
            if root==None:
                return None
            
            if level==0:
                if root.left==None and root.right==None:
                    self.list2.append(root)
            else:
                traversal2(root.left,level-1)
                traversal2(root.right,level-1)
        if root==None:
            return []
        elif root.left==None and root.right==None:
            return [str(root.val)]
            
        tall=height(root)
        
        for i in range(tall-1,-1,-1):
            traversal(root,i)
            traversal2(root,i)
            
        list4=[]
        list5=[]
        
        for i in range(1,len(self.list1)):
            if self.list1[i-1] in self.list2:
                compare=self.list1[i-1]
                list4.append(compare.val)
                for j in range(i,len(self.list1)):
                    if self.list1[j].left==compare or self.list1[j].right==compare:
                        compare=self.list1[j]
                        list4.append(compare.val)
                if list4!=[]:
                    list5.append(list4[::-1])
                list4=[]
        list6=[]        
        for i in list5:
            string=''
            for j in range(len(i)):
                if j!=len(i)-1:
                    string+=(str(i[j])+'->')
                else:
                    string+=str(i[j])
                    
            list6.append(string)
            string=''
        return list6
