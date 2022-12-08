'''
You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.

Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

As a reminder, any shorter prefix of a string is lexicographically smaller.

For example, "ab" is lexicographically smaller than "aba".
A leaf of a node is a node that has no children.

Example 1:

Input: root = [0,1,2,3,4,3,4]
Output: "dba"
'''

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def root_node(root):
            nonlocal string,count,res
            if root==None:
                return None

            string+=dict1[root.val]

            if root.left==None and root.right==None:
                if count==0:
                    res=string[::-1]
                    count+=1
                elif res>string[::-1]:
                    res=string[::-1]

            if root_node(root.left) or root_node(root.right):
                return True

            string=string[0:-1]

            return False

        string=''
        res=''
        count=0

        dict1=dict(zip([i for i in range(26)],['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',\
        's','t','u','v','w','x','y','z']))

        root_node(root)

        return res
