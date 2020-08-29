class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        output_head = ListNode()
        output_tail = output_head
        ten_val = 0
        while l1 or l2:
            if l1 and l2:
                sum = l1.val + l2.val
            else:
                sum = l1.val if l1 else l2.val
            sum += ten_val
            ten_val = sum // 10
            output_tail.next = ListNode(sum % 10)
            output_tail = output_tail.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next 
        if ten_val > 0:
            output_tail.next = ListNode(ten_val)
        return output_head.next
