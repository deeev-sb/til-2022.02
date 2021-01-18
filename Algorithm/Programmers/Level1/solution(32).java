// 완주하지 못한 선수
// 단 한 명의 선수만 완주하지 못한 상황이므로, 완주 리스트를 기준으로 비교하면 됨

import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        Arrays.sort(participant);
        Arrays.sort(completion);
        for (int i = 0; i < completion.length; i++){
            if (!(completion[i].equals(participant[i])))
                return participant[i];
        }
        return participant[participant.length-1];
    }
}