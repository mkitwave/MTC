// 모의고사
// https://programmers.co.kr/learn/courses/30/lessons/42840

import java.util.ArrayList;
class Solution {
    public int[] solution(int[] answers) {
        int[] answer = {};
        ArrayList<Integer> list = new ArrayList<Integer>();
        int[] count = new int[3];
        int[] second = new int[]{2, 1, 2, 3, 2, 4, 2, 5};
        int[] third = new int[]{3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        int num=1;
        for(int i=0; i<answers.length; i++){
            if(answers[i]==num){
                count[0]++;
            }
            if(num==5){
                num=1;
            }else{
                num++;
            }
        }
        num=0;
        for(int i=0; i<answers.length; i++){
            if(answers[i]==second[num]){
                count[1]++;
            }
            if(num==7){
                num=0;
            }else{
                num++;
            }
        }
        num=0;
        for(int i=0; i<answers.length; i++){
            if(answers[i]==third[num]){
                count[2]++;
            }
            if(num==9){
                num=0;
            }else{
                num++;
            }
        }
        int max=0;
        for(int i=0; i<count.length; i++){
            if(max<count[i]){
                max=count[i];
            }
        }
        for(int i=0; i<count.length; i++){
            if(max==count[i]){
              list.add(i+1);   
            }
        }
        int[] answer2 = new int[list.size()];
        for(int i=0; i<answer2.length; i++){
            answer2[i] = list.get(i).intValue();
        }
        answer = answer2;
        return answer;
    }
}