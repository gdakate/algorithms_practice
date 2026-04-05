# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        current = head
        
        # 본거 잇는지 확인/ 없으면 seen 셋에 넣음 / while로 봤는지 아닌지 확인
        while current is not None:
            if current in seen:
                return True
            seen.add(current)
            current = current.next
        
        return False
