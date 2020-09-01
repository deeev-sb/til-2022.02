# 두 리스트 합치기

def solution(N, nlist, M, mlist):
    sumlist = sorted(nlist+mlist)
    answer = ''
    for i in range(N+M):
        answer += str(sumlist[i])
    else:
        return answer

N = int(input())
nlist = list(map(int, input().split()))
M = int(input())
mlist = list(map(int, input().split()))

print(solution(N, nlist, M, mlist))