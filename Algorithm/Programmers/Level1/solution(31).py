# K번째수

def solution(array, commands):
    answer = []
    array_test = array
    for i in range(len(commands)):
        array_test = array[commands[i][0]-1:commands[i][1]]
        array_test = sorted(array_test)
        answer.append(array_test[commands[i][2]-1])
    return answer
