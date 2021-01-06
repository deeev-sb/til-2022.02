// 정수 내림차순으로 배치하기

import java.util.*;

class Solution {
    public long solution(long n) {
        long answer = 0;
        String[] arr = (String.valueOf(n)).split("");
        String result = "";
        Arrays.sort(arr);
        Collections.reverse(Arrays.asList(arr));
        for (String s : arr)
            result += String.valueOf(s);
        answer = Long.valueOf(result);
        return answer;
    }
}