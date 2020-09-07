# Section 3. 탐색&시뮬레이션 (string, 1차원, 2차원 리스트 탐색)

**📋 Table of Contents**
- [Section 3. 탐색&시뮬레이션 (string, 1차원, 2차원 리스트 탐색)](#section-3-탐색시뮬레이션-string-1차원-2차원-리스트-탐색)
  - [1. 회문 문자열 검사](#1-회문-문자열-검사)
    - [방법 1.](#방법-1)
    - [방법 2.](#방법-2)
  - [2. 숫자만 추출](#2-숫자만-추출)
  - [3. 카드 역배치](#3-카드-역배치)
  - [4. 두 리스트 합치기](#4-두-리스트-합치기)
  - [5. 수들의 합](#5-수들의-합)
  - [6. 격자판 최대합](#6-격자판-최대합)
  - [7. 사과나무](#7-사과나무)
  - [8. 곳감(모래시계)](#8-곳감모래시계)
  - [9. 봉우리](#9-봉우리)
  - [10. 스도쿠 검사](#10-스도쿠-검사)
  - [11. 격자판 회문수](#11-격자판-회문수)
    - [회문 길이가 고정되어 있을 때](#회문-길이가-고정되어-있을-때)
    - [회문 길이가 가변적일 때](#회문-길이가-가변적일-때)

<br />

## 1. 회문 문자열 검사

### 방법 1.

```python
n = int(input())
for i in range(n):
    s = input()
    s = s.upper()
    size = len(s)
    for j in range(size//2):
        if s[j] != s[-1-j]:
            print("#%d NO" %(i+1))
            break
    else:
        print("%d YES" %(i+1))
```

### 방법 2.

```python
# 파이썬스럽게!
n = int(input())
for i in range(n):
    s = input()
    s = s.upper()
    if s == s[::-1]:
        print("#%d YES" %(i+!))
    else:
        print("#%d NO" %(i+!))
```

👉 [내 코드 보러가기](../solve/section_3/solution_1.py)

포맷팅을 쓰면 더 쉽게 출력 가능! 까먹지말자 포맷팅 😢

문자열[::-1]을 활용해 reverse된 문자열을 구할 수 있음!! 😮

## 2. 숫자만 추출

```python
s = input()
for x in s:
    if x.isdecimal(): # 0부터 9까지의 숫자만 확인
        res=res*10+int(x)
print(res)
cnt = 0
for i in range(1, res+1):
    if res%i == 0:
        cnt += 1
print(cnt)
```

👉 [내 코드 보러가기](../solve/section_3/solution_2.py)

isdigit()는 모든 숫자가 포함될 수 있는데, isdecimal()은 0부터 9까지만 확인하므로 여기서는 isdecimal()을 사용하는 게 더 나음

## 3. 카드 역배치

```python
a = list(range(21))
for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i] = a[e-i], a[s+i]
a.pop(0)
for x in a:
    print(x, end = ' ')
```

👉 [내 코드 보러가기](../solve/section_3/solution_3.py)

pop(0)를 사용하면 리스트 맨 앞의 요소를 제거할 수 있음! 기억해두자 😋

## 4. 두 리스트 합치기

```python
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
p1 = p2 = 0
c = []
while p1<n and p2<m:
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1
if p1<n:
    c = c + a[p1:]
if p2<n:
    c = c + a[p2:]
for x in c:
    print(x, end=' ')
```

👉 [내 코드 보러가기](../solve/section_3/solution_4.py)

이미 정렬이 되어 있으므로 sort를 사용할 필요가 없음!

이미 정렬되어 있는 상태이기 때문에 O(n)만에 결괏값을 구할 수 있는데, sort를 사용하면 O(nlogn) 걸림.

## 5. 수들의 합

```python
n, m = map(int, input().split())
a = list(map(int, input().split()))
lt = 0
rt = 1
tot = a[0]
while True:
    if tot<m:
        if rt<n:
            tot += a[rt]
            rt += 1
        else:
            break
    elif tot==m:
        cnt += 1
        tot -= a[lt]
        lt += 1
    else:
        tot -= a[lt]
        lt += 1
print(cnt)
```

👉 [내 코드 보러가기](../solve/section_3/solution_5.py)

처음에 이중 for문으로 풀었는데, 5번 테스트케이스가 타임아웃이 발생하여 강의의 문제 설명 부분을 듣고 코드 구현

## 6. 격자판 최대합

```python
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)] # 이차원 리스트 받는 법
largest = -2147000000
for i in range(n):
    sum1 = sum2 = 0 # sum1은 행의 합, sum2는 열의 합 저장
    for j in range(n):
        sum1 += a[i][j]
        sum2 += a[j][i]
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2
sum1 = sum2 = 0 # 두 대각선의 합 저장
for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n-i-1]
if sum1 > largest:
    largest = sum1
if sum2 > largest:
    largest = sum2
print(largest)
```

👉 [내 코드 보러가기](../solve/section_3/solution_6.py)

이차원 리스트 입력 받는 방법 기억해두기!! 😆

함께 수행해도 되는 코드는 묶어서 반복시키자 🙁

## 7. 사과나무

```python
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
res = 0
s = e = n//2
for i  in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i < n//2 :
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1
print(res)
```

👉 [내 코드 보러가기](../solve/section_3/solution_7.py)

## 8. 곳감(모래시계)

```python
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
for i in range(m):
    h, t, k = map(int, input().split())
    if t==0: # 왼쪽으로 회전
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0)) # 맨 앞의 요소를 빼서 맨 뒤에 추가
    else: # 오른쪽으로 회전
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop()) # 맨 뒤의 요소를 빼서 맨 앞에 추가
res = 0
s = 0
e = n-1
for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i < n//2 :
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
print(res)
```

👉 [내 코드 보러가기](../solve/section_3/solution_8.py)

pop()과 insert()를 잘 사용할 줄 알면 매우 쉬운 문제...!!!! 😦

## 9. 봉우리

```python
# 상하좌우 확인을 위한 dx, dy 리스트 생성
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
# 테두리 생성
a.insert(0, [0]*n)
a.append([0]*n)
for x in a:
    x.insert(0, 0)
    x.append(0)
cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt += 1
print(cnt)
```

👉 [내 코드 보러가기](../solve/section_3/solution_9.py)

if에 and로 다 묶을 필요 없이 dx, dy 리스트를 생성하고 all을 사용해서 확인하는 방법도 있음!

## 10. 스도쿠 검사

```python
def check(a):
    for i in range(9):
        ch1=[0]*10
        ch2=[0]*10
        for j in range(9):
            ch1[a[i][j]]=1
            ch2[a[j][i]]=1
        if sum(ch1)!=9 or sum(ch2)!=9:
            return False
    for i in range(3):
        for j in range(3):
            ch3=[0]*10
            for k in range(3):
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]]=1
            if sum(ch3)!=9:
                return False
    return True

a=[list(map(int, input().split())) for _ in range(9)]
if check(a):
    print("YES")
else:
    print("NO")
```

👉 [내 코드 보러가기](../solve/section_3/solution_10.py)

## 11. 격자판 회문수

### 회문 길이가 고정되어 있을 때
```python
board=[list(map(int, input().split())) for _ in range(7)]
cnt=0
for i in range(3):
    for j in range(7):
        tmp=board[j][i:i+5]
        if tmp==tmp[::-1]:
            cnt+=1
        for k in range(2):
            if board[i+k][j]!=board[i+5-k-1][j]:
                break;
        else:
            cnt+=1   
print(cnt)
```

### 회문 길이가 가변적일 때

```python
board=[list(map(int, input().split())) for _ in range(7)]
cnt=0
len=5
for i in range(3):
    for j in range(7):
        tmp=board[j][i:i+len]
        if tmp==tmp[::-1]:
            cnt+=1
        #tmp=board[i:i+5][j] 앞 행은 리스트가 아니라서 슬라이스가 안된다.
        for k in range(len//2):
            if board[i+k][j]!=board[len-k+i-1][j]:
                break;
        else:
            cnt+=1
        
print(cnt)
```

👉 [내 코드 보러가기](../solve/section_3/solution_11.py)


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