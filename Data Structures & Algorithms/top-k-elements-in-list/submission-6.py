class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        n = len(nums)

        #복습 Round : key 대상함수 / get()말고 get
        return sorted(count, key = count.get  , reverse = True)[:k]
