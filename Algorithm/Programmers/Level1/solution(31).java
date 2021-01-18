// K번째수
// array가 들어오면 거기서 원하는 구간을 자르고 그 구간 내에 있는 k번째 수를 출력하는 형태
// 배열 구간 슬라이싱 문제로 copyOfRange를 활용하면 된다!

import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        for (int i = 0; i < commands.length; i++){
            int[] temp = Arrays.copyOfRange(array, commands[i][0]-1, commands[i][1]);
            Arrays.sort(temp);
            answer[i] = temp[commands[i][2]-1];
        }
        return answer;
    }
}