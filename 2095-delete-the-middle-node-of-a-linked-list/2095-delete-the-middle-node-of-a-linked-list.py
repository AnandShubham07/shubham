# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        count=0
        ptr=head
        while(ptr!=None):
            count+=1
            ptr=ptr.next
        mid=int(count/2)
        if(mid==0):
            head=None
            return head
        c=0
        ptr=head
        while(ptr!=None):
            if(c==mid-1):
                ptr.next=ptr.next.next
            c+=1
            ptr=ptr.next
        
        return head



        