# 노가다 : 이중포문으로 타겟 되는거 구함 근데 o(1)이래
# 자료구조 : 리스트. 투포인터 -> 왼오에서돌아감? 타겟보다


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while left<right:

            if numbers[left]+numbers[right]==target:
                return[left+1,right+1]
            elif numbers[left]+numbers[right]<target:
                left+=1
            elif numbers[left]+numbers[right]>target:
                right -=1

        