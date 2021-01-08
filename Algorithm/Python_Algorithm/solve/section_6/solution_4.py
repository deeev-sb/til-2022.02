# 합이 같은 부분집합 (DFS)
import sys
def DFS(L, partial_sum):
    if partial_sum > total//2:
        return
    if partial_sum == (total - partial_sum):
        print("YES")
        sys.exit(0)
    if L < n:
        DFS(L + 1, partial_sum + nlist[L])
        DFS(L + 1, partial_sum)

if __name__=="__main__":
    n = int(input())
    nlist = list(map(int, input().split()))
    total = sum(nlist)
    if total%2 == 0 :
        DFS(0, 0)
    print("NO")