# 최댓값과 최솟값

def solution(s):
    answer = ''
    s_num = s.split(' ')
    num = []
    
    for i in s_num:
        num.append(int(i))
    
    num = sorted(num)
    
    answer = str(num[0]) + ' ' + str(num[-1])
    
    return answer
