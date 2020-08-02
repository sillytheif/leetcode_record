class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        flag = head
        if head.next==None:
            return head
        second = head.next
        r = None
        while second:
            flag.next = r
            r = flag
            flag = second
            second = second.next
        flag.next = r
        return flag