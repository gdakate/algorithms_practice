class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while left<right:
            ad = numbers[left]+numbers[right]
            if ad== target:
                return [left+1,right +1]
            elif ad <target:
                left+=1
            elif ad>target :
                right -=1
        return False
