/* 모의고사
https://programmers.co.kr/learn/courses/30/lessons/42840#qna */

function solution(answers) {
  var answer = [];
  var num1_cnt = 0; var num2_cnt = 0; var num3_cnt = 0;
  var num1 = [1, 2, 3, 4, 5];
  var num2 = [2, 1, 2, 3, 2, 4, 2, 5];
  var num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
  
  //1번
  var j = -1;
  for(var i = 0; i < answers.length; i++){
      j++;
      if(num1[j]===answers[i]){
          num1_cnt++;
      }
      if(j===num1.length-1){
          j = -1;
      }
  }
  
  //2번
  j = -1;
  for(var i = 0; i < answers.length; i++){
      j++;
      if(num2[j]===answers[i]){
          num2_cnt++;
      }
      if(j===num2.length-1){
          j = -1;
      }
  }
  
  //3번
  j = -1;
  for(var i = 0; i < answers.length; i++){
      j++;
      if(num3[j]===answers[i]){
          num3_cnt++;
      }
      if(j===num3.length-1){
          j = -1;
      }
  }
  
  var max = Math.max(num1_cnt, num2_cnt, num3_cnt);
  if(max === num1_cnt) {answer.push(1);}
  if(max === num2_cnt) {answer.push(2);}
  if(max === num3_cnt) {answer.push(3);}
  
  return answer;
}