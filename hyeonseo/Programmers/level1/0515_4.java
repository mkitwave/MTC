// 같은 숫자는 싫어
// https://programmers.co.kr/learn/courses/30/lessons/12906

import java.util.ArrayList;

public class Solution {
    public int[] solution(int []arr) {
        int[] answer = {};
        int temp=-1;
        ArrayList<Integer> list = new ArrayList<Integer>();
        for(int i=0; i<arr.length; i++){
            if(!(temp==arr[i])){
                list.add(arr[i]);
                temp=arr[i];
            }
        }
        int[] answer2 = new int[list.size()];
        for(int i=0; i<answer2.length; i++){
            answer2[i]=list.get(i).intValue();
        }
        answer=answer2;
        return answer;
    }
}