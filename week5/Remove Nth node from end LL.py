class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        tail=dummy
        while tail.next:
            if tail.next.val == val:
                tail.next= tail.next.next
            else:
                tail = tail.next    
        return dummy.next        