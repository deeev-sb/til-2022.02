# Section 5. 자료구조 활용 (스택, 큐, 해쉬, 힙)

**📋 Table of Contents**
- [Section 5. 자료구조 활용 (스택, 큐, 해쉬, 힙)](#section-5-자료구조-활용-스택-큐-해쉬-힙)
  - [1. 가장 큰 수 (스택)](#1-가장-큰-수-스택)
  - [2. 쇠막대기 (스택)](#2-쇠막대기-스택)
  - [3. 후위 표기식 만들기 (스택)](#3-후위-표기식-만들기-스택)
  - [4. 후위 연산 (스택)](#4-후위-연산-스택)
  - [5. 공주구하기 (큐)](#5-공주구하기-큐)
  - [6. 응급실 (큐)](#6-응급실-큐)
  - [7. 교육과정설계 (큐)](#7-교육과정설계-큐)
  - [8. 단어찿기 (해쉬)](#8-단어찿기-해쉬)
  - [9. 아나그램](#9-아나그램)
    - [9.1 딕셔너리 해쉬](#91-딕셔너리-해쉬)
    - [9.2 리스트 해쉬](#92-리스트-해쉬)
  - [10. 최소힙](#10-최소힙)
  - [11. 최대힙](#11-최대힙)
  
<br />

## 1. 가장 큰 수 (스택)

```python
num, m=map(int, input().split())
num=list(map(int, str(num)))
stack=[]
for x in num:
    while stack and m>0 and stack[-1]<x:
        stack.pop()
        m-=1
    stack.append(x)
if m!=0:
    stack=stack[:-m]
res=''.join(map(str, stack))
print(res)
```

👉 [내 코드 보러가기](../solve/section_5/solution_1.py)

## 2. 쇠막대기 (스택)

```python
s=input()
stack=[]
cnt=0
for i in range(len(s)):
    if s[i]=='(': # 여는 괄호면 그냥 추가
        stack.append(s[i])
    else:
        stack.pop()
        if s[i-1]=='(': # 레이저인 경우
            cnt+=len(stack)
        else: # 그냥 닫힌 경우
            cnt+=1
print(cnt)
```

👉 [내 코드 보러가기](../solve/section_5/solution_2.py)

## 3. 후위 표기식 만들기 (스택)

```python
a=input()
stack=[]
res=''
for x in a:
    if x.isdecimal(): # 10진수 숫자인지 확인
        res+=x
    else:
        if x=='(':
            stack.append(x)
        elif x=='*' or x=='/':
            while stack and (stack[-1]=='*' or stack[-1]=='/'):
                res+=stack.pop()
            stack.append(x)
        elif x=='+' or x=='-':
            while stack and stack[-1]!='(': # '(' 직전까지 pop()
                res+=stack.pop()
            stack.append(x)
        elif x==')':
            while stack and stack[-1]!='(': # '(' 직전까지 pop()
                res+=stack.pop() # '(' 제거
            stack.pop()
while stack:
    res+=stack.pop()
print(res)
```

👉 [내 코드 보러가기](../solve/section_5/solution_3.py)

## 4. 후위 연산 (스택)

```python
a=input()
stack=[]
for x in a:
    if x.isdecimal():
        stack.append(int(x))
    else: # 두번째로 pop한 숫자와 첫번째로 pop한 숫자 순으로 계산해야 함
        if x=='+':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2+n1)
        elif x=='-':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2-n1)
        elif x=='*':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2*n1)
        elif x=='/':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2/n1)
print(stack[0])
```

👉 [내 코드 보러가기](../solve/section_5/solution_4.py)

## 5. 공주구하기 (큐)

```python
from collections import deque

n, k=map(int, input().split())
q=list(range(1, n+1))
dq=deque(q)
while dq:
    for _ in range(k-1):
        cur=dq.popleft()
        dq.append(cur)
    dq.popleft()
    if len(dq)==1:
        print(dq[0])
        dq.popleft()
```

👉 [내 코드 보러가기](../solve/section_5/solution_5.py)

## 6. 응급실 (큐)

```python
from collections import deque

n, m=map(int, input().split())
# 인덱스 출력을 위해 enumerate 사용
Q=[(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
Q=deque(Q)
cnt=0
while True:
    cur=Q.popleft()
    if any(cur[1]<x[1] for x in Q):
        Q.append(cur)
    else:
        cnt+=1
        if cur[0]==m:
            print(cnt)
            break
```

👉 [내 코드 보러가기](../solve/section_5/solution_6.py)

index 번호가 필요할 땐 `enumerate`를 활용하자!

## 7. 교육과정설계 (큐)

```python
from collections import deque

need=input()
n=int(input())
for i in range(n):
    plan=input()
    dq=deque(need)
    for x in plan:
        if x in dq:
            if x!=dq.popleft(): # 필수 과목 순서가 잘못됨
                print("#%d NO" %(i+1))
                break
    else:
        if len(dq)==0:
            print("#%d YES" %(i+1))
        else: # 필수 과목을 모두 듣지 않음
            print("#%d NO" %(i+1))
```

👉 [내 코드 보러가기](../solve/section_5/solution_7.py)

## 8. 단어찿기 (해쉬)

```python
import sys

n=int(input())
p=dict()
for i in range(n):
    word=input()
    p[word]=1 # value 값을 1로 초기화
for i in range(n-1):
    word=input()
    p[word]=0 # 사용한 단어의 value 값을 0으로 변경
for key, val in p.items():
    if val==1: # value 값이 1이면 사용하지 않은 단어
        print(key)
        break
```

👉 [내 코드 보러가기](../solve/section_5/solution_8.py)

## 9. 아나그램

### 9.1 딕셔너리 해쉬

```python
a=input()
b=input()
sH=dict()
for x in a:
    sH[x]=sH.get(x, 0)+1
for x in b:
    sH[x]=sH.get(x, 0)-1

for x in a:
    if(sH.get(x)>0): # 두 문자열이 일치하면 value 값이 0이어야 함
        print("NO")
        break;
else:
    print("YES")
```

### 9.2 리스트 해쉬

```python
a=input()
b=input()
# 아스키넘버 활용
str1=[0]*52
str2=[0]*52
for x in a:
    if x.isupper():
        str1[ord(x)-65]+=1 # ord는 아스키넘버 출력
    else:
        str1[ord(x)-71]+=1
for x in b:
    if x.isupper():
        str2[ord(x)-65]+=1
    else:
        str2[ord(x)-71]+=1
for i in range(52):
    if str1[i]!=str2[i]: # 두 리스트의 값이 일치하는지 확인
        print("NO")
        break
else:
    print("YES")
```

👉 [내 코드 보러가기](../solve/section_5/solution_9.py)

## 10. 최소힙

```python
import heapq as hq

a=[]
while True:
    n=int(input())
    if n==-1:
        break
    if n==0:
        if len(a)==0:
            print(-1)
        else:
            print(hq.heappop(a))
    else:
        hq.heappush(a, n)
```

👉 [내 코드 보러가기](../solve/section_5/solution_10.py)

## 11. 최대힙

```python
import heapq as hq

a=[]
while True:
    n=int(input())
    if n==-1:
        break
    if n==0:
        if len(a)==0:
            print(-1)
        else:
            print(-hq.heappop(a))
    else:
        hq.heappush(a, -n)
```

👉 [내 코드 보러가기](../solve/section_5/solution_11.py)

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