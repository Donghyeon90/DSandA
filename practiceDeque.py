import collections

#This deque is provided by the python's collections.
#You can build stack, queue, or linkedlist with the deque.

#Stack
#The idea of the stack is last in first out (LIFO)
s= collections.deque()
s.append(1)
s.append(2)
s.append(3) #1,2,3
print(s) # 1,2,3
#By using the pop function, you can get the last one out.
s.pop() #1,2
print(s) #1,2

#Queue
#The idea of the queue is first in first out. 
s=collections.deque()
s.append(1)
s.append(2)
s.append(3)
print(s) #1,2,3
#By using the popleft function, you can get the first one out (FIFO)
s.popleft()
print(s) #2,3

#Linked list
#The idea of the linked list, you can append at the front or end.
#Also, you can get the first element or last element out. 
s=collections.deque()
s.append(1)
s.append(2)
s.append(3)
s.appendleft(0)
print(s) #0,1,2,3
s.popleft() #1,2,3
print(s)
s.pop() #1,2
print(s)

#By using the deque, you can implement the stack, the queue, and the linked list.
