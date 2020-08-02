class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        flag = ListNode(0)
        flag.next = head
        last_temp = flag
        temp = head
        while temp!=None:
            if temp.val == val:
                last_temp.next = temp.next
                temp = temp.next
            else:
                last_temp = last_temp.next
                temp =temp.next
        return flag.next
