'''Given a sorted array. Convert it into a Height balanced Binary Search Tree (BST). Find the preorder traversal of height balanced BST. If there exist many such balanced BST consider the tree whose preorder is lexicographically smallest.
Height balanced BST means a binary tree in which the depth of the left subtree and the right subtree of every node never differ by more than 1.

Example 1:

Input: nums = {1, 2, 3, 4}
Output: {2, 1, 3, 4}
Explanation: 
The preorder traversal of the following 
BST formed is {2, 1, 3, 4}:
           2
         /   \
        1     3
               \
                4
                '''

class Solution:
    def __init__(self):
        self.list1=[]
	def sortedArrayToBST(self, nums):
	    def buildBST(nums,start,end):
	       if start>end:
	        return None
	            
	       mid=(start+end)//2
	       
	       self.list1.append(nums[mid])
	       
	       left=buildBST(nums,start,mid-1)
	       right=buildBST(nums,mid+1,end)
	       
	       return self.list1
	       
	    return buildBST(nums,0,len(nums)-1)
