# 노가다 : 하나씩 꺼내서 이중포문으로 나보다 큰거 언제 잇나 보고 반환 
# 자료구조 : 스택으로 어케함? -> 날씨보단 인덱스를 저장함. 

# 현재 날씨 인덱스로 스택에 저장. 
# 현재 날씨가 스택 저장 날씨보다 크면 스택 탑 pop, 인덱스 차이를 결과 인덱스에 저장
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack =[]
        output = [0]* len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                prev = stack.pop()
                output[prev]= i-prev
            stack.append(i)
                
        return output

        