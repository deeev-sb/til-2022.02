# 침몰하는 타이타닉 (그리디)

def solution(n, m, people):
    people.sort()
    cnt = 0
    while people:
        if len(people) == 1:
            cnt += 1
            break
        if people[0] + people[-1] <= m:
            cnt += 1
            people.pop(0)
            people.pop()
        else:
            cnt += 1
            people.pop()
    return cnt

n, m = map(int, input().split())
people = list(map(int, input().split()))
print(solution(n, m, people))