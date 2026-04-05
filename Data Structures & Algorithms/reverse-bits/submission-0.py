class Solution:
    def reverseBits(self, n: int) -> int:
        sum =0
        for i in range(32):
            bit = (n>>i)&1
            sum += bit <<(31-i) #bit를 저만큼 왼으로 밀어서 역으로 갖다넣음
        
        return sum #파이썬은 그냥 출력 십진수로 해줌

    