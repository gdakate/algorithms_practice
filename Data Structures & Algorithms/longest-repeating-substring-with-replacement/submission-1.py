#노가다 : 윈도우로.. 오 늘려가며 중복이게.. ? 셋 길이 늘어나면 왼제거? 근데 그 다음도 봐야지.

# 딕셔너리 사용 : 값-나온횟수.
# dic에 잇는지확인, 없으면 만들고 추가, 최대 나온값도 확인
# while 창 크기 - 자주 나온값 차이 >k (= 바꿔야할게 k보다 많다는뜻)이면 왼 이동, 지우기

#샤갈 어려워
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
      l = 0
      maxlen =0
      maxfre =0
      seen = {}
      for r in range(len(s)):
        seen[s[r]]=seen.get(s[r],0)+1
        maxfre = max(maxfre, seen[s[r]])

        while (r-l+1)- maxfre >k :
            seen[s[l]]-=1
            l+=1
        
        maxlen = max(r-l+1,maxlen)
      return maxlen