# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head ==None:
            return []
        if head.next==None:
            return head
        #import pdb;pdb.set_trace()
        temp_1 = head
        flag = head.next
        temp_before =None
        while temp_1!=None and temp_1.next!=None:

            temp_2 = temp_1.next
            temp_1.next = temp_2.next
            temp_2.next = temp_1
            if temp_before!=None:
                temp_before.next = temp_2
            temp_before = temp_1
            temp_1 = temp_1.next
        return flag


def init_node(l):
    head = ListNode(l[0])
    temp = head
    for i in range(1,len(l)):
        temp.next = ListNode(l[i])
        temp =temp.next
    return head
def print_node(head):
    temp =head
    while temp!=None:
        print(temp.val)
        temp = temp .next
mm = init_node([1,2,3,4])
a =Solution()
answer = a.swapPairs(mm)
print_node(answer)
