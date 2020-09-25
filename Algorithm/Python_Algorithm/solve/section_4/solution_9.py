# 증가수열 만들기 (그리디)

def solution(n, num):
    if num[0] > num[-1]:
        temp = num.pop()
        answer = 'R'
    else:
        temp = num.pop(0)
        answer = 'L'
    
    while num:
        if len(num) == 1 and num[0] > temp:
            answer += 'L'
        if num[0] <= num[-1] and num[0] > temp:
            temp = num.pop(0)
            answer += 'L'
        elif num[0] > num[-1] and num[-1] > temp:
            temp = num.pop()
            answer += 'R'
        elif num[0] > temp:
            temp = num.pop(0)
            answer += 'L'
        elif num[-1] > temp:
            temp = num.pop()
            answer += 'R'
        else:
            break
    print(len(answer))
    print(answer)

n = int(input())
num = list(map(int, input().split()))
solution(n, num)