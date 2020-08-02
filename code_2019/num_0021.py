# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp_1 = l1
        temp_2 = l2
        new_head = ListNode(0)
        temp = new_head
        while temp_1 != None and temp_2 != None:
            if temp_1.val < temp_2.val:
                temp.next = temp_1
                temp = temp.next
                temp_1 = temp_1.next
            else:
                temp.next = temp_2
                temp = temp.next
                temp_2 = temp_2.next

        if temp_1 != None:
            temp.next = temp_1
        else:
            temp.next = temp_2
        return new_head.next