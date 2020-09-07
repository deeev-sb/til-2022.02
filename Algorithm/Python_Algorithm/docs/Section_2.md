# Section 2. 코드 구현력 기르기

**📋 Table of Contents**
- [Section 2. 코드 구현력 기르기](#section-2-코드-구현력-기르기)
  - [0. 선수지식 - 최솟값 구하기](#0-선수지식---최솟값-구하기)
  - [1. K번째 약수](#1-k번째-약수)
  - [2. K번째 수](#2-k번째-수)
  - [3. K번째 큰 수](#3-k번째-큰-수)
  - [4. 대표값](#4-대표값)
  - [5. 정다면체](#5-정다면체)
  - [6. 자릿수의 합](#6-자릿수의-합)
    - [방법 1.](#방법-1)
    - [방법 2.](#방법-2)
  - [7. 소수 (에라토스테네스 체)](#7-소수-에라토스테네스-체)
  - [8. 뒤집은 소수](#8-뒤집은-소수)
  - [9. 주사위 게임](#9-주사위-게임)
  - [10. 점수 계산](#10-점수-계산)

<br />

## 0. 선수지식 - 최솟값 구하기

1. 초기화를 무한대로

    ```python
    arr=[5, 3, 7, 9, 2, 5, 2, 6]
    arrMin=float('inf') # 가장 큰 값으로 초기화
    for i in range(len(arr)):
        if arr[i]<arrMin:
            arrMin=arr[i]
    print(arrMin)
    ```

2. 첫 번째 인덱스 수로 초기화

    ```python
    arr=[5, 3, 7, 9, 2, 5, 2, 6]
    arrMin=arr[0
    for i in range(1, len(arr)):
        if arr[i]<arrMin:
            arrMin=arr[i]
    print(arrMin)
    ```

3. range 대신 arr로 바로 받아오는 방법

    ```python
    arr=[5, 3, 7, 9, 2, 5, 2, 6]
    arrMin=float('inf') # 가장 큰 값으로 초기화
    for i in arr:
        if x<arrMin:
            arrMin=x
    print(arrMin)
    ```

## 1. K번째 약수

```python
n, k = map(int, input().split())
cnt = 0
for i in range(1, n+1):
    if n%i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else:
    print(-1)
```

👉 [내 코드 보러가기](../solve/section_2/solution_1.py)

## 2. K번째 수

```python
T = int(input())
for t in range(T):
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = a[s-1:e]
    a.sort()
    print("#%d %d" %(t+1, a[k-1]))
```

👉 [내 코드 보러가기](../solve/section_2/solution_2.py)

포맷팅을 쓰면 더 쉽게 출력 가능! 까먹지말자 포맷팅 😢

## 3. K번째 큰 수

```python
n, k = map(int, input().split())
a = list(map(int, input().split()))
res=set()
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i]+a[j]+a[m])
res = list(res)
res.sort(reverse=True)
print(res[k-1])
```

👉 [내 코드 보러가기](../solve/section_2/solution_3.py)

set 쓰는 법이 헷갈려서 안썼는데 이제 확실히 기억해두자!!


## 4. 대표값

```python
n = int(input())
a = list(map(int, input().split()))
ave = int(sum(a)/n + 0.5)
min = 2147000000
for idx, x in enumerate(a):
    tmp = abs(x-ave)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp==min:
        if x > score:
            score = x
            res = idx + 1
print(ave, res)
```

👉 [내 코드 보러가기](../solve/section_2/solution_4.py)

- `round` 를 쓸 때 `import math` 를 안해도 됨!
- python의 `round` 가 `round_half_even` 방식을 채택하고 있기 때문에 `round(4.500)` 를 출력하면 `4` 가 출력되고 `round(5.500)` 를 출력하면 `6` 이 되므로 `round` 를 쓰면 안됨 ㅠㅠ <br />
⇒ 평균에 `0.5` 를 더하고 `int` 형으로 변환시켜주는 방법이 BEST!
- `enumarate()` 를 사용하면 `index number` 를 받아올 수 있음!!!!!


## 5. 정다면체

```python
n, m = map(int, input().split())
cnt = [0]*(n+m+3) # 왜 더하기 3인지 이해가 안되는데..
for i in range(1, n+1):
   for j in range(1, m+1):
      cnt[i+j] += 1
max = -247000000
for i in range(n+m+1):
    if cnt[i]>max:
        max=cnt[i]
for i in range(n+m+1):
    if cnt[i]==max:
        print(i, end=' ')
```

👉 [내 코드 보러가기](../solve/section_2/solution_5.py)


## 6. 자릿수의 합

### 방법 1.

```python
n = int(input())
a = list(map(int, input().split()))

def digit_sum(x):
    sum = 0
    while x>0:
        sum += x%10
        x = x//10
    return sum

max=-2147000000
for x in a : # 리스트에 있는 값을 하나하나 넘김
    tot = digit_sum(x)
    if tot > max:
        max = tot
        res = x
print(res)
```

### 방법 2.

```python
n = int(input())
a = list(map(int, input().split()))

def digit_sum(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum

max=-2147000000
for x in a : # 리스트에 있는 값을 하나하나 넘김
    tot = digit_sum(x)
    if tot > max:
        max = tot
        res = x
print(res)
```

👉 [내 코드 보러가기](../solve/section_2/solution_6.py)


## 7. 소수 (에라토스테네스 체)

```python
n = int(input())
ch = [0]*(n+1)
cnt = 0
for i in range(2, n+1):
    if ch[i]==0:
        cnt += 1
        for j in range(i, n+1, i):
            ch[j]=1
print(cnt)
```

👉 [내 코드 보러가기](../solve/section_2/solution_7.py)

## 8. 뒤집은 소수

```python
def reverse(x):
    res = 0
    while x>0:
        t = x%10
        res = res*10 + t
        x = x//10
    return res

def isPrime(x):
    if x==1:
        return False
    # 1과 자기 자신(x)를 제외한 약수가 존재하는지 확인
    # 약수가 존재하는지는 절반까지만 확인하면 됨!
    for i in range(2, x//2+1):
        if x%i == 0:
            return False
    else:
        return True

n = int(input())
a = list(map(int, input().split()))
for x in a :
    time = reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')
```

👉 [내 코드 보러가기](../solve/section_2/solution_8.py)

## 9. 주사위 게임

```python
n = int(input())
for i in range(n):
    tmp = input().split()
    tmp.sort()
    a, b, c = map(int, tmp)
    if a==b and b==c:
        money = 10000 + a+1000
    elif a==b or a==c:
        money = 1000+(a*100)
    elif b==c:
        money = 1000+(b*100)
    else:
        money = c*100
    if money>res:
        res=money
print(res)

'''
개인적인 생각이지만 입력받는 숫자가 3개로 제한되어있고,
sort()를 사용해 정렬한 숫자들을 비교할거면 elif를 저렇게 나눌 필요가 없는 듯
''' 
```

👉 [내 코드 보러가기](../solve/section_2/solution_9.py)

## 10. 점수 계산

```python
n = int(input())
a = list(map(int, input().split())
sum = 0
cnt = 0
for x in a:
    if x==1:
        cnt += 1
        sum += cnt
    else:
        cnt = 0
print(sum)
```

👉 [내 코드 보러가기](../solve/section_2/solution_10.py)

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