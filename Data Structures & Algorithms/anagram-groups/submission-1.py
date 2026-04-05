#노가다 : 다 sorted돌려서 seen에 없으면 저장, 있으면 seen에서 갖오기 , 근데 출력은?
# 자료구조 : List

# list - sorted애들 key로 만들고 값으로 원래 값 넣음(append). 없으면 빈거 만들기

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for s in strs:
            key = "".join(sorted(s)) # sorted한거는 문자 한개씩 떨어져잇어서 일케함

            if key not in group:
                group[key]=[]
            
            group[key].append(s)

        return list(group.values())
                