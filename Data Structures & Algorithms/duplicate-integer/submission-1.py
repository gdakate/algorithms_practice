# 1.입력/출력 뭐지?
# 2.노가다로 풀면 어케 할지 - 다 돌려서 겹치는거 잇음 true
# 3.노가다 줄여줄 자료구조 뭘지 - Set 사용 -> 중복 제거해줌

# note : sort로 중복제거하여 길이 차이 확인  
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        new = set(nums)
        if len(new)== len(nums):
            return False
        else:
            return True