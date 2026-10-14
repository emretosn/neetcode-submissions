# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev, cur = None, slow.next
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        slow.next = None

        while prev:
            tmp1 = head.next
            head.next = prev
            tmp2 = prev.next
            prev.next = tmp1
            
            head = tmp1
            prev = tmp2