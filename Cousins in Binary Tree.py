'''Problem Description:
Given a Binary Tree A consisting of N nodes.

You need to find all the cousins of node B.
Input 1:

 A =

           1
         /   \
        2     3
       / \   / \
      4   5 6   7 

B = 5
Output 1:
[6, 7]'''

class Solution:
    def solve(self, root, B):
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
                if root.left:
                    list2.append(root.left.val)
                    list1.append([root.left.val,root.val])
                if root.right:
                    list2.append(root.right.val)
                    list1.append([root.right.val,root.val])
            else:
                traversal(root.left,level-1)
                traversal(root.right,level-1)
        tall=height(root)
        list1=[]
        list2=[]
        for i in range(tall):
            traversal(root,i)

            if B in list2:
                for i in list1:
                    if i[0]==B:
                        parent=i[1]

                list3=[]

                for i in list1:
                    if i[1]!=parent:
                        list3.append(i[0])
                return list3

            list1=[]
            list2=[]
