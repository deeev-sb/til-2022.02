# 창고정리(그리디)

def solution(l, num, m):
    for _ in range(m):
        num.sort()
        num[0] += 1
        num[-1] -= 1
    return max(num)-min(num)

l = int(input())
num = list(map(int, input().split()))
m = int(input())
print(solution(l, num, m))