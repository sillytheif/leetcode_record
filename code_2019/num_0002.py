class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        head  = ListNode(0)
        temp_node = head
        carry = 0
        while l1 != None or l2 !=None:
            if l1 != None:
                l1_val = l1.val
                l1 =l1.next
            if l2 != None:
                l2_val = l2.val
                l2 = l2.next

            temp_sum = carry + l1_val +l2_val
            carry = temp_sum //10
            temp_node.next = ListNode(temp_sum%10)
            temp_node = temp_node.next
            l1_val = 0
            l2_val = 0
        if carry>0:
            temp_node.next = ListNode(1)
        return head.next




def design_list_node(l1):
    head = ListNode(int(str_l1[-1]))
    #import pdb;pdb.set_trace()
    temp =head
    if len(str_l1) ==1:
        return head
    else:
        for i in range(2,len(str_l1)+1):
            temp.next = ListNode(int(str_l1[-i]))
            if i == len(str(str_l1)):
                return head
            else:
                temp =temp.next



pp =Solution()
l1 = design_list_node(1000000000000000000000000000001)
l2 = design_list_node(465)
answer= pp.addTwoNumbers(l1,l2)

while True:
    print(answer.val)
    if answer.next == None:
        break
    else:
        answer =answer.next
