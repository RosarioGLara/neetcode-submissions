# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        node = None
        while head.next is not None:
            next_node = head.next
            head.next = node
            node = head
            head = next_node
        
        head.next = node

        return head