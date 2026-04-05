#노가다 : 왼 0 오를 늘려감, 겹치는거 잇음 맥스 기록하고 왼을 이동, 오 초기화
#자료구조 : set으로 문자관리, right을 for로 관리, while 오가 잇으면 ->중복, 왼 제거
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left =0
        maxlen =0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left +=1
            seen.add(s[right])
            maxlen = max(right-left+1,maxlen)
        return maxlen