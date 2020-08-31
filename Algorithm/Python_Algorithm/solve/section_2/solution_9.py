# 주사위 게임

def solution(num):
    num.sort()
    if num[0] == num[2]:
        return 10000 + num[0]*1000
    elif num[0] == num[1] or num[1] == num[2] :
        return 1000 + num[1]*100
    else:
        return max(num)*100

N = int(input())
max_money = 0
for i in range(N):
    num = list(map(int, input().split()))
    money = solution(num)
    if money > max_money:
        max_money = money
else:
    print(max_money)