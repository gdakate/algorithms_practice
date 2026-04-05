# 1.입력/출력 뭐지?
# 2.노가다로 풀면 어케 할지 - 이중포문으로 다 돌려서 더하기?
# 3.노가다 줄여줄 자료구조 뭘지 - hash쓰라는데?

# 보완(comp) = target - nums[i] 로 설정
# 이미 본적있으면 가져오기 없으면 seen에 넣기
# seen의 인덱스를 num의 값으로, seem의 값을 num의 인덱스로 !!!

# hash: 뭔가 찾기 위해 저장해두고 쓴다. dic or list
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # 숫자라서 dic

        for i in range(len(nums)):
            comp = target-nums[i]

            if comp in seen:
                return [seen[comp],i]
            
            seen[nums[i]]=i