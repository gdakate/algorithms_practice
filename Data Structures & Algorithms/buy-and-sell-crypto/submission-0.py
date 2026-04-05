#노가다 :이중포문으로 하나잡고 가면서 차이를 저장함. 가장 차이 큰 인덱스로 기기
#자료구조 : 슬라이딩 윈도, left 늘리고 조건 깨지면 줄이기?

# left =0, right =1 정하고, while right<len 동안
# left,right 차이계산, max 저장, right이 더 작으면 l,r바꾸기
# r은 매번 게속 증가 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left =0
        right = 1
        maxx =0

        while right < len(prices):
            if prices[left]<prices[right]:
                maxx = max(prices[right]-prices[left],maxx)
            elif prices[left]>prices[right]:
                left=right
            right +=1
        
        return maxx
                
