class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_streak =0
        num = set(nums)

        for i in nums:
            streak =0
            curr = i
            while curr in num:
                streak +=1
                curr +=1
            max_streak = max(max_streak, streak)
        
        return max_streak

   # set : 1) 중복 제거 - unique, distinct
   #       2) 존재 여부 확인용 : x in nums(set)      