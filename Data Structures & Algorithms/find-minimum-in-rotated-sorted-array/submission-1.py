# 노가다 : 하나씩 돌아가며 최소값 찾기 
# 자료구조 : binary

#보통 mid = while 안에.
# nums[mid] > nums[right]→ 최솟값은 오른쪽 절반에 있음
# 아니면→ 최솟값은 왼쪽 절반이나 mid에 있음
# 반복하다 보면 left == right가 되고,그 위치가 최소
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        while left<right:
            mid = (left+right)//2
            if nums[mid]>nums[right]:
                left = mid+1
            else:
                right = mid
            
        return nums[left]
            