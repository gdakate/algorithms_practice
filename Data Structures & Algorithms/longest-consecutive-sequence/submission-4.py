
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = sorted(nums)
        length = 1
        longest =1
        if len(nums)==0:
            return 0
        for i in range(1,len(nums)):
            if num[i]==num[i-1]+1:
                length +=1
            elif num[i]-num[i-1]==0:
                continue
            else:
                longest = max(length, longest)
                length = 1
           
        return max(length,longest)
        
