# 뮤직비디오 (결정알고리즘)

def solution(N, M, music):
    lt = music[0]
    rt = sum(music)
    answer = 0
    while lt<=rt:
        m = (lt+rt)//2
        cnt = 1
        temp = 0
        for i in music:
            if (temp + i) > m:
                cnt += 1
                temp = i
            else:
                temp += i
        if cnt <= M and m >= max(music):
            answer = m
            rt = m - 1
        else:
            lt = m + 1

    return answer

N, M = map(int, input().split())
music = list(map(int, input().split()))
print(solution(N, M, music))