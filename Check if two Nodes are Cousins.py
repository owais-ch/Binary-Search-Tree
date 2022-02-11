'''Given the binary Tree of and two-node values. Check whether the two-node values are cousins of each other or not.

Example 1:

Input:
      1
    /   \
   2     3
a = 2, b = 3
Output: 0'''

def isCousin(root, a, b):
    def traversal(root):
        q=deque([])
        q.append(root)
        list1=[]
        list2=[]
        level=0
        while len(q)>0:
            count=len(q)
            while count>0:
                temp=q.popleft()
                
                list1.append(temp.data)
                
                if temp.left:
                    q.append(temp.left)
                    if temp.left.data==a or temp.left.data==b:
                        list2.append([temp.data,level])
                if temp.right:
                    q.append(temp.right)
                    if temp.right.data==a or temp.right.data==b:
                        list2.append([temp.data,level])
                #print(list2)        
                if len(list2)==2:
                    if list2[0][0]!=list2[1][0] and list2[0][1]==list2[1][1]:
                        return True
                    else:
                        return False
                    
                    
                count-=1
            
            level+=1
    
    return traversal(root)
