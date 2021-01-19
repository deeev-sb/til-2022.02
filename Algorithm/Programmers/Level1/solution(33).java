// 모의고사
// 가장 잘 찍은 사람 찾기. 여러명이면 오름차순 정렬
// array와 list를 모두 활용하여 푸는 문제!!

import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] answer = {};
        int[] std1 = {1, 2, 3, 4, 5};
        int[] std2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] std3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        int[] cnt = new int[3];
        
        for (int i = 0; i < answers.length; i++){
            // 수포자1
            if (answers[i]==std1[i%5])
                cnt[0]++;
            // 수포자2
            if (answers[i]==std2[i%8])
                cnt[1]++;
            // 수포자3
            if (answers[i]==std3[i%10])
                cnt[2]++;
        }
        
        // 가장 많이 맞춘 문제 수
        int max = cnt[0];
        for (int i = 1; i < 3; i++)
            if (max < cnt[i])
                max = cnt[i];
        
        // 가장 많이 맞춘 수포자
        List<Integer> std_list = new ArrayList<>();
        for (int i = 0; i < 3; i++)
            if (max == cnt[i])
                std_list.add(i+1);
        
        // 배열에 넣기
        answer = new int[std_list.size()];
        for (int i = 0; i < std_list.size(); i++)
            answer[i] = std_list.get(i);
        
        
        return answer;
    }
}