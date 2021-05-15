/* 완주하지 못한 선수
https://programmers.co.kr/learn/courses/30/lessons/42576 */

function solution(p, c) {
  var answer = '';
  p.sort();                               //정렬하고
  c.sort();
  for (var i = 0; i < p.length; i++){     //돌려서
      if(p[i]!=c[i]){                     //다르면
          answer = p[i];                  //answer에 넣고
          break;                          //즉시 종료
      }
  }
  return answer;
}