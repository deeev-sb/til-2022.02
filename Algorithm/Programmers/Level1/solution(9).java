// 제일 작은 수 제거하기

import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        int[] answer = {};
        ArrayList<Integer> arrlist = new ArrayList<Integer>();
        int min = arr[0];
        
        // 순서 유지를 위해 min을 먼저 찾고 그 다음 제외시키기
        for (int i = 1; i < arr.length; i++){
            if (min > arr[i])
                min = arr[i];
        }
        
        for (int i = 0; i < arr.length; i++){
            if (min != arr[i])
                arrlist.add(arr[i]);
        }
        
        
        if (arrlist.isEmpty())
            arrlist.add(-1);
        
        int n = arrlist.size();
        answer = new int[n];
        for (int i = 0; i < n; i++)
            answer[i] = arrlist.get(i);
        
        return answer;
    }
}