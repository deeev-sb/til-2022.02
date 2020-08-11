# 위장

def solution(clothes):
    answer = 1
    dic = {}

    
    for i in range(len(clothes)):
        if clothes[i][1] in dic:
            dic[clothes[i][1]].append(clothes[i][0])
        else:
            dic[clothes[i][1]] = [clothes[i][0]]
    
    for value in dic.values():
        answer *= len(value) + 1 # 해당 종류의 의상을 입지 않는 경우 포함
    
    return answer - 1 # 안 입은 경우 제외
