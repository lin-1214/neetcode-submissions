# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        dummy = ListNode(0, None)
        head = dummy

        while (list1 or list2):
            # print(list1.val, list2.val)
            if list1 is None:
                head.next = list2
                list2 = list2.next

            elif list2 is None:
                head.next = list1
                list1 = list1.next

            elif (list1.val < list2.val):
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            
            head = head.next

        return dummy.next
        