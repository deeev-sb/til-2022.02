# 완주하지 못한 선수

def solution(participant, completion):
    answer = ''
    # completion은 participant보다 길이가 1 작음
    # 정렬을 통해 같지 않은 것 찾기
    participant = sorted(participant)
    completion = sorted(completion)
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            return answer
    answer = participant[-1]
    return answer
