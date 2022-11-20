'''Given the root of a binary tree, return the most frequent subtree sum. If there is a tie, return all the values with the highest frequency in any order.

The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself).

Example 1:

Input: root = [5,2,-3]
Output: [2,-3,4]'''

class Solution:
    def findFrequentTreeSum(self, root):
        def traversal(root):
            if root==None:
                return 0
            #if root.left==None:
            #    return 0
            #if root.right==None:
            #    return 0
            ls=traversal(root.left)
            rs=traversal(root.right)

            sum1=ls+rs+root.val

            if sum1 not in dict1:
                dict1[sum1]=1
            else:
                dict1[sum1]+=1

            return sum1

        dict1=dict()

        traversal(root)

        max_freq=max(dict1.values())
        return list(filter(lambda x:dict1[x]==max_freq,dict1.keys()))
