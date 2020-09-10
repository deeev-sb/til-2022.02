# 이분검색

def solution(lt, rt, M, array):
    m = (lt+rt)//2
    if array[m]==M:
        return m+1
    elif array[m]>M:
        return solution(lt, m+1, M, array)
    else:
        return solution(m, rt, M, array)

N, M = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
print(solution(0, N, M, array))