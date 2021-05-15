// https://programmers.co.kr/learn/courses/30/lessons/42840

function solution(answers) {
  var answer = [];
  var score = [0, 0, 0];
  var people = [[1, 2, 3, 4, 5], 
                [2, 1, 2, 3, 2, 4, 2, 5], 
                [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]];
  
  for(var i=0; i<answers.length; i++){
      if(answers[i] === people[0][i%5])
          score[0] += 1;
      if(answers[i] === people[1][i%8])
          score[1] += 1;
      if(answers[i] === people[2][i%10])
          score[2] += 1;
  }
  
  var max = Math.max(score[0], score[1], score[2]);
  
  if (max = score[0]){
      answer.push(1);
  }if (max = score[1]){
      answer.push(2);
  }if (max = score[2]){
      answer.push(3);
  }
  
  return answer;
}