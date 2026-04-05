class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #일단 한글자씩 다 비교
        m, n = len(word1), len(word2)
        dp =[[0]*(n+1)for _ in range(m+1)] # for _ 그냥 변수 안쓰는거 뿐 / (n+1)*(m+1) 배열 만듬

        for i in range(m+1) : dp[i][0]=i
        for j in range(n+1) : dp[0][j]=j

        for i in range(1, m+1):
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1] # 같으면 변경할거 없어서 이전거랑 같음
                else :
                    dp[i][j]= 1+ min(
                        dp[i-1][j],#delete ; word1에서 i번째 글자 지움, word2는 그대로
                        dp[i][j-1], #insert ; word1에 word2[j] 글자 추가, word1은 그대로 j-1까지 해결된 비용에 1을 더해줌
                        dp[i-1][j-1]#exchange ; word1[i]를 word2[j]로 바꿈, 둘 다 넘어감 둘다 바뀌니까 둘다 이전비용에 1을 더해줌
                    )
        return dp[m][n]