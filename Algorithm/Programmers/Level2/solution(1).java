// 최댓값과 최솟값

import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        String[] strarr = s.split(" ");
        int n = strarr.length;
        int[] intarr = new int[n];
        
        for (int i = 0; i < n; i++){
            intarr[i] = Integer.valueOf(strarr[i]);
        }
        
        Arrays.sort(intarr);
        
        answer = String.valueOf(intarr[0]) + ' ' + String.valueOf(intarr[n-1]);
        
        return answer;
    }
}