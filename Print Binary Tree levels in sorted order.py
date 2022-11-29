'''Given an array arr[] which contains data of N nodes of Complete Binary tree in level order fashion. The task is to print the level order traversal in sorted order.

Example 1:

Input:
N = 7
arr[] = {7 6 5 4 3 2 1}
Output:
7
5 6
1 2 3 4
Explanation: The formed Binary Tree is:
             7
          /      \
        6         5
      /  \      /   \
     4    3    2     1
'''

class Solution:
    def binTreeSortedLevels (self,arr, n):
        start=0
        i=0
        increment=2**i
        list1=[]
        while start<n:
            list1.append(sorted(arr[start:start+increment]))
            start+=increment
            i+=1
            increment=2**i
            
        return list1
