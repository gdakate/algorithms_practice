class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return sorted(count, key = count.get, reverse = True)[:k]

# sorted(대상, key = 기준 함수, reverse = True/False)
# Slicing: [:2] front two
        
            

        