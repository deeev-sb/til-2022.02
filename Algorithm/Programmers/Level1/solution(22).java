// 자연수 뒤집어 배열로 만들기

import java.util.*;

class Solution {
    public int[] solution(long n) {
        int[] answer = {};
        String[] arr = (String.valueOf(n)).split("");
        Collections.reverse(Arrays.asList(arr));
        
        answer = new int[arr.length];
        
        for (int i = 0; i < arr.length; i++)
            answer[i] = Integer.valueOf(arr[i]);
        
        return answer;
    }
}