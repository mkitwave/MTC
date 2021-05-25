// https://programmers.co.kr/learn/courses/30/lessons/68644

function solution(numbers) {
  var answer = [];
  for (var i = 0; i < numbers.length; i++) {
      for(var j = i+1; j < numbers.length; j++){
          var sum = numbers[i] + numbers[j];
          //배열 속에 해당 원소가 있는지 확인
          if (!answer.includes(sum)){
              answer.push(sum);
          }
      }
  }
  answer.sort((a,b)=> a - b);
  return answer;
}