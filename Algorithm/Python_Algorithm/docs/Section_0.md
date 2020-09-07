# Section 0. 파이썬 기초 문법 (선수지식)

**📋 Table of Contents**
- [Section 0. 파이썬 기초 문법 (선수지식)](#section-0-파이썬-기초-문법-선수지식)
  - [1. 변수와 출력함수](#1-변수와-출력함수)
    - [1.1 변수](#11-변수)
    - [1.2 출력함수](#12-출력함수)
    - [1.3 주석](#13-주석)
    - [1.4 값 교환](#14-값-교환)
    - [1.5 변수 타입](#15-변수-타입)
  - [2. 변수입력과 연산자](#2-변수입력과-연산자)
  - [3. 조건문 (if분기법, 다중if문)](#3-조건문-if분기법-다중if문)
    - [3.1 if문](#31-if문)
    - [3.2 중첩 if문](#32-중첩-if문)
    - [3.3 if 분기법](#33-if-분기법)
    - [3.4 다중 if문](#34-다중-if문)
  - [4. 반복문 (for, while, break, continue)](#4-반복문-for-while-break-continue)
    - [4.1 for문](#41-for문)
    - [4.2 while문](#42-while문)
    - [4.3 break](#43-break)
    - [4.4 continue](#44-continue)
  - [5. 반복문을 이용한 문제 풀이](#5-반복문을-이용한-문제-풀이)
  - [6. 중첩 반복문 (2중 for문)](#6-중첩-반복문-2중-for문)
  - [7. 문자열과 내장함수](#7-문자열과-내장함수)
  - [8. 리스트와 내장함수(1)](#8-리스트와-내장함수1)
  - [9. 리스트와 내장함수(2)](#9-리스트와-내장함수2)
  - [10. 2차원 리스트 생성과 접근](#10-2차원-리스트-생성과-접근)
  - [11. 함수 만들기](#11-함수-만들기)
  - [12. 람다함수](#12-람다함수)

<br />

## 1. 변수와 출력함수

### 1.1 변수

- 데이터를 저장하는 공간
- 변수명 정하기
    1. 영문과 숫자, _로 이루어짐
    2. 대소문자 구분
    3. 문자나 _로 시작 (숫자로 시작 X)
    4. 특수문자를 사용하면 안됨 (&, % 등)
    5. 키워드(예약어) 사용하면 안됨 (if, for 등)

### 1.2 출력함수

- 출력은 `print()` 사용
- print() 안에 변수가 아닌 문자나 숫자를 넣어서 출력 가능
- print(a, b, c) 이런 식으로 `,` 를 사용하여 구분하며 자동 띄워쓰기가 됨
- 문자와 숫자 함께 출력 가능 (`,` 로 구분해주면 됨!)
- `sep` 를 사용하면 `,` 로 구분된 변수 사이의 출력 형식 지정 가능
- print는 기본적으로 끝에 `\n` 이 포함되어 있음
- 끝에 포함된 `\n` 을 변경하려면 `end` 를 사용하면 됨

```python
print("number") # number
a, b, c, = 1, 2, 3
print(a, b, c) # 1 2 3 (, 를 사용하면 자동으로 띄워쓰기됨)
print("number", a, b, c) # number 1 2 3 (문자와 숫자 함께 출력 가능)
print("number : ", a, b, c) # number :  1 2 3
print(a, b, c, sep='') # abc (seperate를 사용하면 숫자 출력 방식을 정할 수 있음)
print(a, b, c, sep=', ') # a, b, c
print(a, end=' ') # 기본적으로 포함되어 있는 \n 을 ' '로 변경 
```

### 1.3 주석

- 한 줄 주석은 `#` 사용
- 여러 줄 주석은 `'''` 을 사용하면 됨

```python
# 한 줄 주석

'''
여러 줄 주석
'''
```

### 1.4 값 교환

```python
a, b = 10, 20
print(a, b) # 10 20
a, b = b, a # 값 교환 방법은 매우 간단함!!
print(a, b) # 20 10
```

### 1.5 변수 타입

- `print(type(a))` 이런 식으로 변수 a의 변수형을 알 수 있음

```python
a = 12345
print(type(a)) # <class 'int'>
```

- 정수형(int) : 12345
- 실수형(float) : 12.345 (8byte만큼만 저장)
- 문자형(str) : 'student' or "student" (`'` 을 쓰든 `''` 쓰든 상관  X)

## 2. 변수입력과 연산자

- 변수입력은 `input` 함수를 이용하여 받음
- 한 번에 여러 개를 받을 때 `split()` 사용
- `input` 함수는 기본적으로 문자열로 받아옴
- 정수형으로 받아오려면 `map` 사용
- 실수형과 정수형을 사칙연산하면 범위가 더 큰 실수형으로 결괏값이 나옴

```python
a = input("숫자를 입력하세요 : ")
# 2
print(a) # 2

a, b = input("숫자를 입력하세요 :").split() # 입력 시 띄워쓰기로 두 변수에 구분하여 넣어줌
# 2 3
print(a + b) # 23

a, b = map(int, input("슷자를 입력하세요: ").split())
# 3 2
print(a+b)  # 5
print(a-b)  # 1
print(a*b)  # 6
print(a/b)  # 1.5
print(a//b) # 1 (몫 연산자)
print(a%b)  # 1 (나머지 연산자)
print(a**b) # 9 (거듭제곱, b만큼 거듭제곱함)
```

## 3. 조건문 (if분기법, 다중if문)

### 3.1 if문

- 조건에 `참` 인 경우 수행됨
- 들여쓰기(indent)를 잘 맞춰야 함!!

```python
x = 7
if x==7 : # 해당 조건이 참이면 아래 print 실행
    print("Lucky")
# Lucky
```

### 3.2 중첩 if문

- if문 안에 if문이 들어가는 형식

```python
x = 15
if x>=10 :
    if x%2==1 :
        print("10이상의 홀수")
# x는 15이므로 print가 출력됨
# x가 12면 10이상이라는 조간은 만족하지만 홀수가 아니므로 print되는 값이 없음
# x가 9이면 첫 번째 조건이 맞지않기 때문에 출력값이 없음
```

- if 안에 if만 존재한다면 논리연산자를 통해 한 줄로 묶어줄 수 있음

```python
if x>0 :
    if x<10 :
        print("10보다 작은 자연수")

# 위의 중첩 if문을 논리연산자로 묶어 한 줄로 변경한 모습
if x>0 and x<10 :
    print("10보다 작은 자연수")

# 사실 위의 연산은 and 안써도 괜찮음 (python만 가능!)
if 0<x<10 :
    print("10보다 작은 자연수")
```

### 3.3 if 분기법

- `if` 의 조건에 맞지 않은 경우 수행하게 하려면  `else` 를 넣으면 됨

```python
if x>0 :
    print("양수")
else:
    print("음수")
```

### 3.4 다중 if문

- 여러 조건을 사용할 때, `elif` 를 사용함
- 조건을 위에서부터 순서대로 확인하다가 참인 조건이 있으면 그 아래 있는 조건 실행

```python
if x>=90 :
    print('A')
elif x>=80:
    print('B')
elif x>=70 :
    print('C')
elif x>=60 :
    print('D')
else:
    print('F')
```

## 4. 반복문 (for, while, break, continue)

- 반복문을 시작하기 전 `range` 를 알아야 함!

    `range(0,10)` 은 0부터 9까지의 숫자라고 생각하면 됨!

    ⇒ `range(시작숫자, 끝숫자+1)` 이런 느낌

    0부터 시작하는 경우 `range(10)` 이라고 써도 됨

### 4.1 for문

```python
for i in range(10):
    print("hello") # 10번 반복하며, print를 10번 출력

for i in range(10, 0, -1): # 원하는 숫자만큼 감소시킬 수 있음, -2를 넣으면 2씩 작아짐
    print(i) # 10부터 1씩 작아지며, 마지막 출력은 1
```

- `for else` 구문의 경우, `for` 문이 정상적으로 수행되어야만 `else` 가 수행됨

```python
# 이 경우 i==5일 때 for문이 종료되므로, 정상적이지 않은 형태로 for가 종료되었기에 else 수행 X
for i in range(1, 11):
    print(i)
    if i==5:
        break
else:
    print(11)

# 이 경우 정상적으로 for문이 종료되었으므로 else 수행
for i in range(1, 11):
    print(i)
else:
    print(11)
```

### 4.2 while문

```python
i = 1
while i<=10:
    print(i)
    i = i + 1 # while문의 경우 증가함을 넣어줘야 함

# 10부터 1까지 출력하려면
i = 10
while i>=1:
    print(i)
    i = i - 1
```

### 4.3 break

```python
i = 1
while True: # 무한 반복문
    print(i)
    if i==10 : # 조건이 참인 경우
        break  # 반복문을 종료시킴
    i += 1 # +=은 축약어로, i = i + 1과 같은 의미
```

### 4.4 continue

```python
for i in range(1, 11):
    if i%2==0:   # 짝수인 경우
        continue # 조건문의 처음으로 넘어감
    print(i)
```

## 5. 반복문을 이용한 문제 풀이

1. 1부터 N까지 홀수 출력하기

    ```python
    n = int(input())
    for i in range(1, n+1):
        if i%2==1:
            print(i)
    ```

2. 1부터 N까지의 합 구하기

    ```python
    n = int(input())
    sum = 0
    for i in range(1, n+1):
        sum += i
    print(sum)
    ```

3. N의 약수 출력하기

    ```python
    n = int(input())
    for i in range(1, n+1):
        if n%i==0:
            print(i)
    ```

## 6. 중첩 반복문 (2중 for문)

```python
for i in range(5):
    print('i:', i, sep='', end='')
    for j in range(5):
        print('j:', j, sep='', end='')
    print() # 줄바꿈 역할

'''
i:0 j:0 j:1 j:2 j:3 j:4
i:1 j:0 j:1 j:2 j:3 j:4
i:2 j:0 j:1 j:2 j:3 j:4
i:3 j:0 j:1 j:2 j:3 j:4
i:4 j:0 j:1 j:2 j:3 j:4
'''

for i in range(5):
    for j in range(i+1):
        print("*", end=' ')
    print()

'''
*
* *
* * *
* * * *
* * * * *
'''

for i in range(5):
    for j in range(5-i):
        print("*", end=' ')
    print()

'''
* * * * *
* * * *
* * *
* *
*
'''
```

## 7. 문자열과 내장함수

- `upper()` 는 문자열을 대문자로 변경
- `lower()` 는 문자열을 소문자로 변경
- `find()` 를 통해 특정 문자를 찾아 인덱스 번호 반환 (문자열도 인덱스로 접근 가능)
- `count()` 는 특정 문자의 개수 반환
- `[:]` 를 사용하여 문자열을 슬라이스 할 수 있음
- `len()` 은 문자열의 길이를 알려줌
- `isupper()` 나 `islower()` 는 대문자인지 소문자인지 확인
- `isalpha()` 는 알파벳인지 확인 (공백을 무시하고 확인할 때 유용)
- `ord()` 는 받은 문자를 아스키넘버로 반환
- `chr()` 은 받은 아스키넘버를 문자로 반환

```python
msg = "It is Time"
print(msg.upper()) # IT IS ITME (msg를 대문자화 시켜서 출력, 원본은 그대로 유지됨)
print(msg.lower()) # it is time
tmp = msg.upper()
print(tmp) # IT IS TIME
print(tmp.find('T')) # 1 (첫 번째 T의 인덱스 번호를 알려줌)
print(tmp.count('T')) # 2 (T의 개수를 알려줌)
print(msg[:2]) # It
print(msg[3:5]) # is (공백도 인덱스에 포함되어 있음)
print(len(msg)) # 10

# 문자열의 길이만큼 수행하는 반복문
for i in range(len(msg)):
    print(msg[i], end=' ')

'''
I t  i s  T i m e
'''

# 문자열의 문자에 하나하나 접근 가능
for x in msg:
    print(x, end=' ')

'''
I t  i s  T i m e
'''

for x in msg:
    if x.isupper(): # 대문자인 경우 참
        print(x, end=' ')

'''
I T
'''

for x in mag:
    if x.isalpha(): # 알파벳인 경우 참
        print(x, end='')

'''
ItisTime
'''

tmp='AZ'
for x in tmp:
    print(ord(x))

'''
65
90
'''

tmp='az'
for x in tmp:
    print(ord(x))

'''
97
122
'''

tmp=65
print(chr(tmp)) # A
```

## 8. 리스트와 내장함수(1)

- `list` 는 여러 변수 값을 저장할 때 사용
- 비어있는 리스트를 생성하는 방법은 `a = []` 또는 `a = list()`
- `+` 를 통해 두 리스트를 합칠 수 있음
- `append()` 를 사용하여 리스트 끝에 값 추가 가능
- `insert(특정지점, 추가할값)` 을 사용하여 특정 지점에 원하는 값을 추가할 수 있음
- `pop()` 을 사용하여 끝의 값을 가져올 수 있는데, `pop(특정지점)` 을 사용하면 특정 지점의 값을 가져올 수 있음
- `remove(제거할값)` 를 사용하여 원하는 값을 제거할 수 있음
- `index(찾을값)` 는 원하는 값의 인덱스 번호 반환
- `sum()` 는 모든 값을 더해서 반환
- `max()` 는 인자 값 중 최댓값을 찾아줌
- `min()` 은 인자 값 중 최솟값을 찾아줌
- `sort()` 를 사용하면 오름차순 정렬
- `sort(reverse=True)` 를 사용하면 내림차순 정렬
- `clear()` 를 사용하면 리스트를 빈 리스트로 초기화

```python
import random as r

a = []     # 비어있는 list 생성
b = list() # 비어있는 list 생성

# 리스트 초기화 (비어있는 list를 생성하지 않아도 됨)
a = [1, 2, 3, 4, 5]
print(a) # [1, 2, 3, 4, 5]
print(a[0]) # 1 (인텍스 0번 값만 출력)

# range를 활용한 초기화
b = list(range(1,6))
print(b) # [1, 2, 3, 4, 5]

# 리스트 더하기
c = a+b
print(c) # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

a.append(6)
print(a) # [1, 2, 3, 4, 5, 6]

a.insert(3, 7)
print(a) # [1, 2, 3, 7, 4, 5, 6]

a.pop()
print(a) # [1, 2, 3, 7, 4, 5]

a.pop(3)
print(a) # [1, 2, 3, 4, 5]

a.remove(4)
print(a) # [1, 2, 3, 5]

print(a.index(5)) # 3

# a의 값이 많이 변경되었으니 초기화 시켜줄까요 :)
a = list(range(1,11))
print(a) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum(a)) # 55 (리스트의 모든 값을 더해서 출력해줌)
print(max(a)) # 10
print(min(a)) # 1
print(min(7, 5) # 5

# random 모듈을 사용해볼까요 :)
r.shuffle(a) # shuffle을 사용하면 섞어줌
print(a) # [10, 6, 3, 4, 1, 8, 5, 9, 2, 7]

# 정렬
a.sort() # 오름차순
print(a) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a.sort(reverse=True) # 내림차순
print(a) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# 빈 리스트로 초기화
a.clear()
print(a) #[]
```

## 9. 리스트와 내장함수(2)

- 문자열과 같은 방식으로 슬라이스
- 문자열과 같은 방식으로 `len()` 을 사용하여 리스트의 길이를 구함
- 문자열과 같이 인덱스 하나하나에 접근 가능함
- `enumerate()` 를 사용하면 인덱스 번호와 인덱스 값을 함께 출력 가능 (튜플 형태로 출력됨)
    - 튜플이란?
- `all` 은 모든 조건이 참인 경우 true를 반환
- `any` 는 모든 조건 중 하나라도 참인 경우 true를 반환

```python
a = [23, 12, 36, 53, 19]

# 리스트 슬라이스
print(a[:3]) # [23, 12, 36]
print(a[1:4]) # [12, 36, 53]

# 리스트 길이
print(len(a)) # 5

# 값에 접근하는 방법
for i in range(len(a)):
    print(a[i], end=' ')
'''
23 12 36 53 19
'''

for x in a:
    print(x, end=' ')

'''
23 12 36 53 19
'''

for x in a:
    if x%2 == 1:
        print(x, end=' ')

'''
23 53 19
'''

# 인덱스 번호와 인덱스의 값 함께 출력
for x in enumerate(a):
    print(x)

''' 튜플 형식으로 출력됨
(0, 23)
(1, 12)
(2, 36)
(3, 53)
(4, 19)
'''

for x in enumerate(a):
    print(x[0], x[1])

'''
0 23
1 12
2 36
3 53
4 19
'''

# enumerate는 이런 식으로 많이 사용
for index, value in enumerate(a):
    print(index, value)

'''
0 23
1 12
2 36
3 53
4 19
'''

if all(60 > x for x in a):
    print("YES")
else:
    print("NO")

''' a 안의 모든 값이 참
YES
'''

if all(50 > x for x in a):
    print("YES")
else:
    print("NO")

''' a 안의 모든 값이 참이 아님 (53때문에!)
NO
'''

if any(15 > x for x in a):
    print("YES")
else:
    print("NO")

''' a 안의 하나라도 참 (12가 참)
YES
'''

if any(11 > x for x in a):
    print("YES")
else:
    print("NO")

''' a 안의 하나도 참이 아님
NO
'''
```

## 10. 2차원 리스트 생성과 접근

```python
# 1차원 리스트 생성
a = [0]*3
print(a) # [0, 0, 0]

# 2차원 리스트 생성
a = [[0]* for _ in range(3)] # for _ in 이런 식으로 쓰면 변수 없이 진행한다는 의미
print(a) # [[0, 0, 0], [0, 0, 0], [0, 0, 0]] 

''' 2차원 리스트는 표로 생각하는 게 좋음 (아래와 같은 느낌)
0 0 0
0 0 0
0 0 0
'''

a[0][1] = 1
print(a) # [[0, 1, 0], [0, 0, 0], [0, 0, 0]] 
a[1][1] = 2
print(a) # [[0, 1, 0], [0, 2, 0], [0, 0, 0]]

# 표처럼 출력하면 보기 편하겠죠 :)
for x in a:
    print(x)

''' for에 의해 1차원 리스트로 출력
[0, 1, 0]
[0, 2, 0]
[0, 0, 0]
'''

# 1차원 리스트가 아닌 값 하나하나로 출력하고 싶은 경우
for x in a:
    for y in x:
        print(y, end= ' ')
    print()

'''
0 1 0
0 2 0
0 0 0
'''
```

## 11. 함수 만들기

- 함수를 만들 때는 `def` 사용
- 함수를 사용하려면 함수 호출를 해야함
- 특정 작업을 계속해서 반복해야 할 때 함수 사용
- 함수는 `main` 위에 만들어야 함 (안그러면 에러나요!)
- `return` 을 통해 호출한 부분으로 결과를 반환

```python
def add(a, b):
    c = a + b
    print(c)

add(3, 2) # 함수를 호출해야 실행됨
add(5, 7)

'''
5
12
'''

def add(a, b):
    c = a + b
    return c

print(add(3, 2)) # 5 (함수에서 출력하는 것이 아닌 메인 스크립트에서 출력)

def add(a, b):
    c = a + b
    d = a - b
    return c, d # 함수를 여러 개 return 가능

print(add(3, 2)) # (5, 1) (튜플 형태로 출력)

def isPrime(x):
    for i in range(2, x):
        if x%1==0:
            return False # return하면 반복문이 종료됨 (함수를 종료시키므로)
    return True

a = [12, 13, 7, 9, 19]
for y in a:
    if isPrime(y): # 함수에서 True를 리턴하는 경우에만 실행
        print(y, end=' ')

'''
13 7 9
'''
```

## 12. 람다함수

```python
def plus_one(x):
    return x + 1

print(plus_one(1)) # 2

# 람다함수 사용법
plus_two = lambda x: x+2
print(plus_two(1)) # 3

# 람다함수는 내장함수의 인자로 사용할 때 좋음
a=[1, 2, 3]
print(list(map(plus_one, a))) # [2, 3, 4]

# 함수를 만들지 않고 lambda를 사용하면 한 줄로 만들 수 있음
print(list(lambda x: x+1, a))) # [2, 3, 4]
```

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