# 1.입력/출력 뭐지?
# 2.노가다로 풀면 어케 할지 - 이중포문으로 다 돌려서 더하기?
# 3.노가다 줄여줄 자료구조 뭘지 - hash쓰라는데?


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
                