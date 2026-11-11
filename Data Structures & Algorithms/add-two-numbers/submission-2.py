# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        dummy = ListNode(0)
        head = dummy

        while (l1 is not None or l2 is not None or carry == 1):
            
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            s = v1 + v2 + carry
            carry = s // 10
            val = s % 10

            new_node = ListNode(val)
            head.next = new_node
            head = head.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
            


        

