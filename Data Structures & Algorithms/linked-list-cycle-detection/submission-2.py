# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# slow, fast 정의하여 fast가 slow 같아지면 참, 루프 없어지면 거짓
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        return False