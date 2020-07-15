# [1차] 비밀지도
# 2018 KAKAO BLIND RECRUITMENT

def solution(n, arr1, arr2):
    answer = []
    answer1, answer2 = [], []
    
    for i in range(n):
        answer1.append('')
        num = bin(arr1[i])[2:]
        if len(num) < n:
            add = n - len(num)
            for j in range(add):
                answer1[i] += ' '
        for k in num:
            if k == '0':
                answer1[i] += ' '
            else:
                answer1[i] += '#'
    
    for i in range(n):
        answer2.append('')
        num = bin(arr2[i])[2:]
        if len(num) < n:
            add = n - len(num)
            for j in range(add):
                answer2[i] += ' '
        for k in num:
            if k == '0':
                answer2[i] += ' '
            else:
                answer2[i] += '#'
    
    for i in range(n):
        answer.append('')
        for j in range(n):
            if answer1[i][j] == answer2[i][j]:
                answer[i] += answer1[i][j]
            else:
                if answer1[i][j] == '#' or answer2[i][j] == '#':
                    answer[i] += '#'
  
    return answer
