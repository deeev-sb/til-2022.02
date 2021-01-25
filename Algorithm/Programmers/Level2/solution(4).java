// 최솟값 만들기
// 길이가 같은 두 배열에서 수를 뽑아 곱하는 것을 배열의 길이만큼 반복하였을 때 최솟값이 얼마인지 구하는 문제
// A, B를 정렬하여 A는 순서대로, B는 역순으로 접근하여 계산하면 됨

import java.util.*;

class Solution
{
    public int solution(int []A, int []B)
    {
        int answer = 0;

        Arrays.sort(A);
        Arrays.sort(B);
        
        for (int i = 0; i < A.length; i++)
            answer += (A[i] * B[A.length-i-1]);
        
        return answer;
    }
}