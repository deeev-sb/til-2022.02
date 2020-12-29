// 같은 숫자는 싫어

import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        int[] answer = {};
        ArrayList<Integer> arrlist = new ArrayList<Integer>();
        int temp = -1;
        for (int i = 0; i < arr.length; i++){
            if (temp != arr[i]){
                arrlist.add(arr[i]);
                temp = arr[i];
            }
        }
        
        int n = arrlist.size();
        answer = new int[n];
        for (int i = 0; i < n; i++){
            answer[i] = arrlist.get(i);
        }
        

        return answer;
    }
}