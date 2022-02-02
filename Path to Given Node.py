'''Problem Description

Given a Binary Tree A containing N nodes.

You need to find the path from Root to a given node B.

NOTE:

No two nodes in the tree have same data values.
You can assume that B is present in the tree A and a path always exists.'''


class Solution:
    def __init__(self):
        self.list1=[]
    def solve(self, root, B):
        def traversal(root):
            if root.left:
                traversal(root.left)

            if root.right:
                traversal(root.right)

            self.list1.append(root)

        traversal(root)
        list2=[]
        length=len(self.list1)
        i=0
        while i<length:
            
            if self.list1[i].val==B:
                list2.append(self.list1[i])
            elif list2!=[]:
                if self.list1[i].left==list2[-1] or self.list1[i].right==list2[-1]:
                    list2.append(self.list1[i])

            i+=1

        list2=[i.val for i in list2]
        #print(B)
        return list2[::-1]
