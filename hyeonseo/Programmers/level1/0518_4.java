// https://programmers.co.kr/learn/courses/30/lessons/12948
// 핸드폰 번호 가리기

class Solution {
    public String solution(String phone_number) {
        String answer = "";
        for(int i=0; i<phone_number.length()-4; i++){
            answer += "*";
        }
        answer += phone_number.substring(phone_number.length()-4);
        return answer;
    }
}