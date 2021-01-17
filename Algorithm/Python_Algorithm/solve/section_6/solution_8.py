# 순열 구하기 (DFS)

def DFS(idx):
    global cnt
    if idx == m:
        if (len(set(temp[:m])) == m):
            for i in range(m):
                print(temp[i], end=' ')
            print()
            cnt += 1
    else:
        for i in range(1, n+1):
            temp[idx] = i
            DFS(idx + 1)

if __name__=="__main__":
    n, m = map(int, input().split())
    temp = [1]*n
    cnt = 0
    DFS(0)
    print(cnt)