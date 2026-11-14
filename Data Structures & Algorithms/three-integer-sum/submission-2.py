class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        outputs =[]
        
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left<right:
                num = nums[left]+nums[right]
                if nums[i]+num == 0:
                     
                    outputs.append([nums[i],nums[left], nums[right]])
                    left+=1
                    right -=1
                    while left < right and nums[left] == nums[left-1]:   # ② 같은 값 left는 건너뜀
                        left += 1
                elif nums[i]+num >0 :
                    right -=1
                elif nums[i]+num<0:
                    left+=1
        return outputs
                    


