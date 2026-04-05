# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 뒤집기 할때 저거 4줄 그냥 외우기

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        prev =None
        curr = head

        while curr:
            nex = curr.next
            curr.next = prev # 뒤집기
            prev = curr # 이전은 이제 현재가 됨
            curr = nex #이동
        return prev