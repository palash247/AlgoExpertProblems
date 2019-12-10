# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# before seeing the solution
# def removeKthNodeFromEnd(head, k):
#     # Write your code here.
#     depth = len_linked_list(head)-k
#     current = head
#     while depth-1 > 0:
#         depth-=1
#         current=current.next
#     if current==head:
#         if depth==0:
#             head.value = head.next.value
#             head.next = head.next.next
#         else:
#             head.next = head.next.next
#     else:
#         current.next = current.next.next
    
# def len_linked_list(head):
#     current = head
#     depth = 0
#     while current:
#         current = current.next
#         depth+=1
#     return depth

# after seeing the solution
def removeKthNodeFromEnd(head, k):
    first = head
    second = head
    while k>0:
        second = second.next
        k-=1
    if not second:
        head.value = head.next.value
        head.next = head.next.next
        return
    while second.next:
        first = first.next
        second = second.next
    first.next = first.next.next
