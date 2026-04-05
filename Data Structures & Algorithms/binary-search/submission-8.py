#노가다 : 가운데 값이랑 타겟 비교. 타겟보다 작으면 mid의 오른족이랑 비교 
#자료구조 : mid를 계속 바꿈

# mid 보다 t크면 -> left= mid +1
# mid 보다 t 작으면 -> right = mid -1
# 그리고 새로운 mid만들, while left<=right동안 반복

# target 찾기 : while left <= right
# 경계, 최소, 첫번째 만족 찾기 : while left<right
class Solution:
    def search(self, nums: List[int], target: int) -> int:
       left =0
       right = len(nums)-1

       while left<=right:
        mid = (left+right)//2
        if nums[mid]>target:
            right = mid-1
        elif nums[mid]==target:
            return mid
        else :
            left = mid+1
       return -1    