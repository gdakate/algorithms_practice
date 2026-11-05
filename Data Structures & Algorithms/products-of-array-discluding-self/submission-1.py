class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        numr=[1]*n
        numl=[1]*n
        #나 빼고 전부" 또는 "구간 합/곱을 반복해서 계산" → Prefix/Suffix로 미리 누적해두기
        # i를 제외한 나머지” → 왼쪽 누적 × 오른쪽 누적 (이 문제)
        # 구간 [l, r]의 합을 여러 번 물어봄" → prefix 배열을 만들어두고 prefix[r+1] - prefix[l]
        # 합이 k인 부분 배열 개수" → prefix sum + dict (나중에 나와)
        for i in range(1,n):
            numl[i]=numl[i-1]*nums[i-1] # 항상 내 왼쪽 애(i-1) 곱하기
        for j in range(n-2,-1,-1):
            numr[j]=numr[j+1]*nums[j+1] # 항상 내 오른쪽 애(i+1) 곱하기
        
        output= []
        for k in range(n):
            output.append(numl[k]*numr[k])
        
        return output

        
        
        
