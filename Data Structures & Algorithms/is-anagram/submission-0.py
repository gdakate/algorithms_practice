# 1.입력/출력 뭐지?
# 2.노가다로 풀면 어케 할지 - 정렬해서 첨부터 아예 같은지보기?
# 3.노가다 줄여줄 자료구조 뭘지 - sorted?

# Sorted -> 문자 같은지 비교
# sort 아니고 sorted!!
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s= sorted(s)
        t=sorted(t)

        if s==t :
            return True
        else:
            return False