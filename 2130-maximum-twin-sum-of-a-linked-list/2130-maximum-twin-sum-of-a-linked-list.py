# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        ptr=head
        count=0
        while ptr!=None :
            count+=1
            ptr=ptr.next
        if(count==0):
            return 0
        if (count==2):
            sums=head.val+head.next.val
            return sums
        last=ptr
        ptr=head
        c=1
        while(c<count//2):
            c+=1
            ptr=ptr.next
        half=ptr
        curr=half.next
        prev=None
        while(curr!=None):
            next_node=curr.next
            if(curr.next!=None and curr.next.next==None):
                last=curr.next
                print(last)
            curr.next=prev
            prev=curr            
            curr=next_node


        half.next=last
        nptr=head
        maxi=nptr.val+last.val
        while(last!=None):
            sums=nptr.val+last.val
            if(sums>maxi):
                maxi=sums
            nptr=nptr.next
            last=last.next

        return maxi