class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '[' or i =='{' or i =='(':
                stack.append(i)
            else :
                if not stack: # pop empty 방비
                    return False
                
            if i==']':
                if stack.pop() != '[':
                    return False
            elif i==')':
                if stack.pop() != '(':
                    return False
            elif i=='}':
                if stack.pop() != '{':
                    return False
        # 안남아잇는거 확인
        return len(stack)==0