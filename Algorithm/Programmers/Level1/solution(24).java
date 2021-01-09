// 정수 제곱근 판별

import java.util.*;

class Solution {
    public long solution(long n) {
        long answer = 0;
        //System.out.println((long)Math.pow((long)Math.sqrt(n), 2));
        long temp = (long)Math.pow((long)Math.sqrt(n), 2);
        if (temp == n)
            answer = (long)Math.pow((long)Math.sqrt(n) + 1, 2);
        else
            answer = -1;
        return answer;
    }
}