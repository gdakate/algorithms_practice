# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#더미 하나를 만듬. tail 로 시작시킴
#작은 값은 tail의 다음 값에 넣음. curr헤드가 걍 curr임. 저거 이동
#만약 curr1밖에 없으면 다 넣기
# dummy의 다음 노드부터가 진짜 리스트니까 그걸 반환
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        curr1 = list1
        curr2 = list2

        while curr1 and curr2:
            if curr1.val <curr2.val:
                tail.next = curr1
                curr1=curr1.next
            else:
                tail.next = curr2
                curr2= curr2.next
            tail = tail.next
        if curr1:
            tail.next = curr1
        else:
            tail.next = curr2

        return dummy.next #tail아니고 dummy

        