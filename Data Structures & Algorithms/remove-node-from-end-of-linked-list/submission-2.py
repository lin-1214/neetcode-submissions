# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if (head.next is None):
            return None
        
        first = head
        length = 0

        while (first is not None):
            length += 1
            first = first.next

        second = head
        prev = None
        tar = length - n

        if (tar == 0):
            return head.next

        while (second is not None):
            if (tar == 1):
                prev = second

            if (tar == 0):
                prev.next = second.next
                break

            tar -= 1
            second = second.next

        return head