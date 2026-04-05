#노가다 : 스택에 왼왼왼 넣기 오 나오면 스택 탑 빼서 비교
#자료구조 : 스택

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i =='{' or i=='[' or i=='(':
                stack.append(i)
            else :
                if not stack:
                    return False

                top = stack.pop()
                
                if i=='}' and top!='{':
                    return False
                elif i==')' and top!='(':
                    return False
                elif i==']' and top!='[':
                    return False
        return len(stack)==0