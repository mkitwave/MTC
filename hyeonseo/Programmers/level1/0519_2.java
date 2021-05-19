// https://programmers.co.kr/learn/courses/30/lessons/12940
// 최대공약수와 최소공배수

class Solution {
    public int[] solution(int n, int m) {
        int[] answer = new int[2];
        if(n>m){
            int temp = n;
            n = m;
            m = temp;
        }
        answer[0] = 1;
        for(int i=n; i>=1; i--){
            if(m%i==0&&n%i==0){
                answer[0] = i;
                break;
            }
        }
        answer[1] = n*m/answer[0];
        return answer;
    }
}