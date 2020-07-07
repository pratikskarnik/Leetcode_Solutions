# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3=ListNode(0)
        head=l3
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        while(l1 and l2):
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0
            if val1>=val2:
                head.next=ListNode(val2)
                head=head.next
                l2=l2.next if l2 else None
            else:
                head.next=ListNode(val1)
                head=head.next
                l1=l1.next if l1 else None
        if l1==None:
            while(l2):
                head.next=ListNode(l2.val)
                head=head.next
                l2=l2.next if l2 else None
        else:
            while(l1):
                head.next=ListNode(l1.val)
                head=head.next
                l1=l1.next if l1 else None
            
                
        return l3.next
                
                
        