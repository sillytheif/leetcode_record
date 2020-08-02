# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1:
            return head
        now = head
        count = 0
        while now!=None:
            count+=1
            now=now.next
        guide = ListNode(0)
        guide.next = head
        temp_end = guide

        for i in range(count//k):
            #import pdb;pdb.set_trace()
            for j in range(k-1):
                temp_before = temp_end
                now = temp_end.next
                for x in range(k-1-j):
                    temp_exchange = now.next
                    temp_before.next =  temp_exchange
                    now.next = temp_exchange.next
                    temp_exchange.next = now
                    temp_before = temp_exchange
            for j in range(k-2):
                now = now.next
            temp_end = now
        return  guide.next

class Solution:
    def reverse(self, head):
        if not head: return None, None
        if not head.next: return head, head
        tail, f, r = head, head.next, None
        while f:
            head.next = r
            r = head
            head = f
            f = f.next
        head.next = r
        return head, tail

    def reverseKGroup(self, head, k):
        if not head: return None
        if not head.next or k < 2: return head
        h = t = head
        prv, nxt = None, None
        #     [1->2->3]->[4->5->6]->[7->8]
        #     [3->2->1]->[6->5->4]->[7->8]
        # prv  h     t   nxt
        while True:
            for _ in range(k - 1):
                if t.next:
                    t = t.next
                else:
                    return head

            nxt = t.next
            t.next = None
            h, t = self.reverse(h)
            if not prv:
                head = h
            else:
                prv.next = h
            if not nxt:
                return head
            prv = t
            t.next = nxt
            h = t = nxt



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
mm = init_node([1,2,3,4,5])
a =Solution()
answer = a.reverseKGroup(mm,3)
print_node(answer)