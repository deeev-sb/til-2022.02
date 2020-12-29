// 자릿수 더하기

import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        String n_str = String.valueOf(n);
        String[] n_arr = n_str.split("");
        for (int i = 0; i < n_arr.length; i++){
            answer += Integer.valueOf(n_arr[i]);
        }
        return answer;
    }
}