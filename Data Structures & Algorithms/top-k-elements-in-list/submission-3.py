class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        num = count.most_common(k)
        print(num)
        
        output= []
        for i in range(len(num)):
            output.append(num[i][0])

        return output

        