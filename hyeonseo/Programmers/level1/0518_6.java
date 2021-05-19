// https://programmers.co.kr/learn/courses/30/lessons/12944
// Æò±Õ ±¸ÇÏ±â

class Solution {
    public double solution(int[] arr) {
        double answer = 0;
        for(int a:arr){
            answer += a;
        }
        answer /= arr.length;
        return answer;
    }
}