// 예산
// budget 내에서 각각의 부서에서 요청한 금액의 물품을 구매할 때 최대 몇 개의 부서에 물품을 구매해 줄 수 있는지 구하는 문제

import java.util.*;

class Solution {
    public int solution(int[] d, int budget) {
        int answer = 0;
        
        Arrays.sort(d);
        
        for (int i = 0; i < d.length; i++)
            if (d[i] <= budget){
                budget -= d[i];
                answer++;
            }
        
        return answer;
    }
}