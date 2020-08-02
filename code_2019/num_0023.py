# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = ListNode(0)
        temp = head
        temp_list = [x for x in lists if x!=None ]
        while temp_list!=None:
            max_flag = 0
            max_val = temp_list[max_flag].val
            for i in range(len(temp_list)):
                if temp_list[i].val<max_val:
                    max_val = temp_list[i].val
                    max_flag = i
            temp.next = temp_list[max_flag]
            temp = temp.next
            if temp_list[max_flag].next!=None:
                temp_list[max_flag] = temp_list[max_flag].next
            else:
                temp_list.pop(max_flag)

        return head.next