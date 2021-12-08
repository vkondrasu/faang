class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = l1
        temp2 = l2
        carry = 0
        result = None
        
        while temp1 or temp2:
            c_sum = (temp1.val if temp1 else 0) + (temp2.val if temp2 else 0) + carry
            carry = c_sum // 10
            c_sum = c_sum %10
            
            if result is None:
                result = ListNode(c_sum)
                temp3 = result
            else:
                temp3.next = ListNode(c_sum)
                temp3 = temp3.next
            
            temp1 = temp1.next if temp1 else None
            temp2 = temp2.next if temp2 else None
                
        if carry > 0:
            temp3.next = ListNode(carry)
            
            
        return result
