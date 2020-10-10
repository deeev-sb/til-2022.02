# 단어 찾기 (해쉬)

def solution(word, use):
    for i in word:
        if i not in use:
            return i

n = int(input())
word = []
for _ in range(n):
    word.append(input())
use = []
for _ in range(n-1):
    use.append(input())
print(solution(word, use))