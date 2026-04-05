# 노가다로 하면? - 중간지점 정해서 왼오 같나보기
# 이걸 줄일 자료구조? 투포인터 ! 

# 투포인터 - 왼오 양끝에서 가운데로 오기
# isalnum(): 숫자,문자 아닌 공백, 특수문자에 FALSE
# not isalnum 일때( 공백이면 ) 하나씩 이동
# 왼오 비교시 둘다 lower()하기
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

