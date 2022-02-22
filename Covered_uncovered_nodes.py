'''You are given the root of a binary tree A, you need to return the absolute difference between sum of all covered elements and the sum of all uncovered elements.

In a binary tree, a node is called Uncovered if it appears either on left boundary or right boundary. Rest of the nodes are called covered.'''

class Solution:
    def coveredNodes(self, root):
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
               list1.append(root.val)
            else:
                traversal(root.left,level-1)
                traversal(root.right,level-1)

        tall=height(root)

        list1=[]
        list2=[]
        list3=[]
        for i in range(tall):
            traversal(root,i)
            #print(list1)
            length=len(list1)
            if length==1:
                list2.append(list1[0])
            else:
                for j in range(length):
                    if j==0 or j==length-1:
                        list2.append(list1[j])
                    else:
                        list3.append(list1[j])
            list1=[]
        
        return abs(sum(list2)-sum(list3))
