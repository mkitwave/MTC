// https://programmers.co.kr/learn/courses/30/lessons/77484

function solution(lottos, win_nums) {
  var answer = [];
  var min = lottos.filter(lotto => win_nums.includes(lotto)).length;
  var max = lottos.filter(lotto => 0 === lotto).length + min;
  
  function ranking(lotto){
      if(lotto === 6) return 1;
      else if(lotto === 5) return 2;
      else if(lotto === 4) return 3;
      else if(lotto === 3) return 4;
      else if (lotto === 2) return 5;
      else return 6;
  }
  
  answer.push(ranking(max), ranking(min));
          
  return answer;
}