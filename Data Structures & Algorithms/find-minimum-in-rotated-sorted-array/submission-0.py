# 노가다 : 하나씩 돌아가며 최소값 찾기 
# 자료구조 : binary
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
            