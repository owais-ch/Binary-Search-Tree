'''Given a singly linked list, remove all the nodes which have a greater value on its following nodes.

Example 1:

Input:
LinkedList = 12->15->10->11->5->6->2->3
Output: 15 11 6 3
Explanation: Since, 12, 10, 5 and 2 are
the elements which have greater elements
on the following nodes. So, after deleting
them, the linked list would like be 15,
11, 6, 3.'''

class Solution:
    def compute(self,head):
        n=head
        head=n
        
        list1=[]
        
        while n!=None:
            list1.append(n.data)
            n=n.next
            
        length=len(list1)
        
        maximum=list1[-1]
        list2=[list1[-1]]
        for i in range(-2,-length-1,-1):
            if list1[i]>=maximum:
                list2.append(list1[i])
                maximum=list1[i]
            
        list2.reverse()
        m=Node(list2[0])
        head=m
        
        for i in range(1,len(list2)):
            hh=Node(list2[i])
            m.next=hh
            m=m.next
            
        return head
