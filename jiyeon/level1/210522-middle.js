function solution(s) {
  var answer = '';
  var index = s.length / 2;
  
  if(s.length % 2 == 0){
      answer = s.substr(index-1, 2);
  }
  if(s.length % 2 == 1){
      answer = s.substr(index, 1);
  }
  return answer;
}