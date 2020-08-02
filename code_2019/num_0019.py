class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp = head
        count_all = 0
        while(temp!=None):
            count_all = count_all+1
            temp = temp.next
        temp = head
        count = 0
        target =count_all - n
        if target == 0:
            head = head.next
            return head
        while(temp!=None):
            count =count+1
            if count == target:
                temp.next = temp.next.next
            temp = temp.next
        return head