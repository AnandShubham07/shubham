# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if(head==None):
            return None
        ptro=head
        ptre=head.next
        last=head
        count=0
        while(last!=None):
            count+=1
            if(last.next==None):
                pointer=last
            last=last.next
        if(count==2):
            return head
        l=(count+1) if count%2==0 else count
        c=1
        while(c<l):
            if(c%2==0):                
                pointer.next=ListNode()
                pointer=pointer.next
                pointer.val=value
                c+=1
            else:
                value=ptro.next.val
                ptro.next=ptro.next.next
                ptro=ptro.next
                c+=1
        return head

                


        