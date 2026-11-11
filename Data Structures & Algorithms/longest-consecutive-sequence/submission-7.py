class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        # O(n) -> 정렬x {}에서 있나 확인하기 
        longest =1

        if len(nums)==0:
            return 0

        for i in num:
            length =1
            if i-1 not in num :
                while i+1 in num:
                    i+=1
                    length +=1
                longest  = max(longest, length)
        return max(longest, length)