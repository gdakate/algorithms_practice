class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ''
        for i in strs:
            n = len(i)
            output = output+ str(n)+'#'+i
        return output
    def decode(self, s: str) -> List[str]:
        outputs = []
        i=0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            length = int(s[i:j]) 
            outputs.append(s[j+1:j+length+1])
            i = j+length+1
        return outputs
                
                