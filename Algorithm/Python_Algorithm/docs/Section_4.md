# Section 4. 이분탐색(결정알고리즘) & 그리디 알고리즘

**📋 Table of Contents**
- [Section 4. 이분탐색(결정알고리즘) & 그리디 알고리즘](#section-4-이분탐색결정알고리즘--그리디-알고리즘)
  - [1. 이분 검색](#1-이분-검색)
  - [2. 랜선 자르기 (결정알고리즘)](#2-랜선-자르기-결정알고리즘)
  - [3. 뮤직비디오 (결정알고리즘)](#3-뮤직비디오-결정알고리즘)
  - [4. 마구간 정하기 (결정알고리즘)](#4-마구간-정하기-결정알고리즘)
  - [5. 회의실 배정 (그리디)](#5-회의실-배정-그리디)
  - [6. 씨름 선수 (그리디)](#6-씨름-선수-그리디)
  - [7. 창고 정리 (그리디)](#7-창고-정리-그리디)
  - [8. 침몰하는 타이타닉 (그리디)](#8-침몰하는-타이타닉-그리디)
    - [방법 1.](#방법-1)
    - [방법 2.](#방법-2)
  - [9. 증가 수열 만들기 (그리디)](#9-증가-수열-만들기-그리디)
  - [10. 역수열 (그리디)](#10-역수열-그리디)


<br />

## 1. 이분 검색

```python
n, m = amp(int, input().split())
a = list(map(int, input().split()))

a.sort() # 이분검색을 하기 위해서는 정렬이 되어 있어야 함
lt = 0 # 왼쪽 끝
rt = n - 1 # 오른쪽 끝
while lt <= rt:
    mid = (lt + rt) // 2
    if a[mid] == m:
        print(mid+1)
        break
    elif a[mid] > m:
        rt = mid - 1
    else:
        lt = mid + 1
```

👉 [내 코드 보러가기](../solve/section_4/solution_1.py)

## 2. 랜선 자르기 (결정알고리즘)

```python
def count(len):
    cnt = 0
    for x in Line:
        cnt += (x//len)
    return cnt

k, n = map(int, input().split())
Line = []
res = 0
largest = 0
for i in range(k):
    tmp = int(input())
    Line.append(tmp)
    largest = max(largest, tmp)
lt = 1
rt = largest
while lt<=rt:
    mid = (lt+rt)//2
    if count(mid) >= n:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)
```

👉 [내 코드 보러가기](../solve/section_4/solution_2.py)

## 3. 뮤직비디오 (결정알고리즘)

```python
def Count(capacity):
    cnt=1
    sum=0
    for x in Music:
        if sum+x>capacity:
            cnt+=1
            sum=x
        else:
            sum+=x
    return cnt

n, m=map(int, input().split())
Music=list(map(int, input().split()))
maxx=max(Music)
lt=1
rt=sum(Music)
res=0
while lt<=rt:
    mid=(lt+rt)//2
    if mid>=maxx and Count(mid)<=m:
        res=mid
        rt=mid-1
    else:
        lt=mid+1
print(res)
```

👉 [내 코드 보러가기](../solve/section_4/solution_3.py)

오랜만에 풀었더니 감이 안잡혀서 푸는 방법 강의 참고 ☹️


## 4. 마구간 정하기 (결정알고리즘)

```python
def Count(len):
    cnt=1
    ep=Line[0]
    for i in range(1, n):
        if Line[i]-ep>=len:
            cnt+=1
            ep=Line[i]
    return cnt

n, c=map(int, input().split())
Line=[]
for _ in range(n):
    tmp=int(input())
    Line.append(tmp)
Line.sort()
lt=1
rt=Line[n-1]
while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=c:
        res=mid
        lt=mid+1
    else:
        rt=mid-1

print(res)
```

👉 [내 코드 보러가기](../solve/section_4/solution_4.py)

## 5. 회의실 배정 (그리디)

```python
# 회의의 끝나는 시간이 중요!!
n = int(input())
meeting = []
for i in range(n):
    s, e = map(int, input().split())
    metting.append((s,e))

# lambda를 사용하여 sort의 우선 순위를 정해줌 (x[1]가 1순위, x[0]가 2순위)
metting.sort(key = lambda x : (x[1], x[0]))
et = 0
cnt = 0
for s, e in meeting:
    if s >= et:
        et = e
        cnt += 1
print(cnt)
```

👉 [내 코드 보러가기](../solve/section_4/solution_5.py)

충분히 생각해보고 범위 지정하자 ☹️

## 6. 씨름 선수 (그리디)

```python
# 키순으로 세운 다음에 몸무게만 비교 (위쪽 사람과 비교)
n = int(input())
body = []
for i in range(n):
    a, b = map(int, input().split())
    body.append((a,b))
body.sort(reverse=True)
largest = 0
cnt = 0
# x는 키, y는 몸무게
for x, y in body:
    if y > largest:
        largest = y
        cnt += 1
print(cnt)
```

👉 [내 코드 보러가기](../solve/section_4/solution_6.py)

## 7. 창고 정리 (그리디)

```python
L = int(input())
a = list(map(int, input().split()))
m = int(input())
a.sort()
for _ in range(m):
    a[0] += 1
    a[L-1] -= 1
    a.sort()
print(a[L-1]-a[0])
```

👉 [내 코드 보러가기](../solve/section_4/solution_7.py)

## 8. 침몰하는 타이타닉 (그리디)

### 방법 1.

```python
n, limit = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
cnt = 0
while p:
    if len(p) == 1:
        cnt += 1
        break
    if p[0] + p[-1] > limit:
        p.pop()
        cnt += 1
    else:
        p.pop(0)
        p.pop()
        cnt += 1
print(cnt)
```

### 방법 2.

deque를 이용한 방법이 조금 더 효율적임!

```python
from collections import deque
n, limit = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
p = deque(p)
cnt = 0
while p:
    if len(p) == 1:
        cnt += 1
        break
    if p[0] + p[-1] > limit:
        p.pop()
        cnt += 1
    else:
        p.popleft()
        p.pop()
        cnt += 1
print(cnt)
```

👉 [내 코드 보러가기](../solve/section_4/solution_8.py)

## 9. 증가 수열 만들기 (그리디)

```python
n = int(input())
a = list(map(int, input().split())
lt = 0
rt = n-1
last = 0
res = ""
tmp = []
while lt<=rt:
    if a[lt] > last:
        tmp.append((a[lt], 'L'))
    if a[rt] > last:
        tmp.append((a[rt]. 'R'))
    tmp.sort()
    if len(tmp) == 0:
        break
    else:
        res = res + temp[0][1]
        last = tmp[0][0]
        if tmp[0][1]=='L':
            lt += 1
        else:
            rt -= 1
    tmp.clear()
print(len(res))
print(res)
```

👉 [내 코드 보러가기](../solve/section_4/solution_9.py)

## 10. 역수열 (그리디)

```python
n = int(input())
a = list(map(int, input().split()))
seq = [0]*n
for i in range(n):
    for j in range(n):
        if a[i]==0 ans seq[j]==0:
            seq[j] = i+1
            break
        elif seq[j]==0:
            a[i] -= 1
for x in seq:
    print(x, end=' ')
```

👉 [내 코드 보러가기](../solve/section_4/solution_10.py)

<br />

---

**📋 index**
- [Section 0. 파이썬 기초 문법(선수지식)](./Section_0.md)
- [Section 1. 강의자료 (문제파일, 소스파일, 채점파일)](https://www.inflearn.com/course/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8)
- [Section 2. 코드 구현력 기르기](./Section_2.md)
- [Section 3. 탐색&시뮬레이션 (string, 1차원, 2차원 리스트 탐색)](./Section_3.md)
- [Section 4. 이분탐색(결정알고리즘)&그리디 알고리즘](./Section_4.md)
- [Section 5. 자료구조 활용(스택, 큐, 해쉬, 힙)](./Section_5.md)
- [Section 6. 완전탐색 (백트래킹, 상태트리와 CUT EDGE)-DFS(깊이우선탐색) 기초](./Section_6.md)
- [Section 7. 깊이/넓이 우선 탐색 (DFS/BFS) 활용](./Section_7.md)
- [Section 8. Dynamic Programming (동적계획법)](./Section_8.md)
- [Section 9. 블록 게임 만들기 (총 7회) : 시뮬레이션 (격자탐색과 DFS 활용)](./Section_9.md)

<br />

> 본 포스팅은 [파이썬 알고리즘 문제풀이 (코딩테스트)](https://www.inflearn.com/course/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8)를 수강하며 작성된 글입니다.