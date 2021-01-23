// 체육복
// lost는 체육복을 도난 당한 학생, reserve는 여벌의 체육복이 있는 학생
// 체격순으로 번호를 매겼으며, 체육복은 바로 앞번호나 뒷번호 학생에게만 빌려줄 수 있음
// 체육복을 입은 총 학생 수를 return
// 여벌의 체육복이 있는 학생도 도난을 당했을 수도 있음!

import java.util.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = n - lost.length;
        
        // 순서가 다르게 들어올 수 있으므로 정확한 확인을 위해 정렬 필요
        Arrays.sort(lost);
        Arrays.sort(reserve);
    
        // 도난 당했지만 여벌의 체육복이 있는 경우 빌려줄 수 없으므로 이 조건부터 확인
        for (int i = 0; i < lost.length; i++){
            for (int j = 0; j < reserve.length; j++){
                if (lost[i] == reserve[j]){
                    answer++;
                    lost[i] = -1;
                    reserve[j] = -1;
                }
            }
        }
        
        // 체육복 빌려주기
        for (int i = 0; i < lost.length; i++){
            for (int j = 0; j < reserve.length; j++){
                if (lost[i] == reserve[j] - 1 || lost[i] == reserve[j] + 1){
                    answer++;
                    lost[i] = -1;
                    reserve[j] = -1;
                }
            }
        }
        System.out.println(Arrays.toString(lost));
        System.out.println(Arrays.toString(reserve));

        return answer;
    }
}