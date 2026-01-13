# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        l3=dummy
        carry=0
        while l1 or l2 or carry:
            num1=l1.val  if l1 else 0 
            num2=l2.val  if l2 else 0
            
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next

            summation=num1+num2+carry
            carry=summation//10
            act_store=summation%10
            l3.next=ListNode(act_store)
            l3=l3.next
        if carry:
            l3.next=ListNode(carry)
           
        return dummy.next