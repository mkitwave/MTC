/* 두 개 뽑아서 더하기
https://programmers.co.kr/learn/courses/30/lessons/68644 */

function solution(numbers) {
  var answer = new Array();
  var firstnum;
  var sum;
  /*
  1. 배열만큼 for문 돌기
  2. 첫번째 숫자 삭제 & 자른 값 따로 저장
  3. 첫번째 숫자 + 나머지
  4. 중복 제거
  5. 다시 1개가 사라진 배열에 2~4 작업
  6. 정렬
  */
  for(var i = numbers.length - 1; i > 0; i--){ 
      firstnum = numbers.shift();               //첫자리 자르기 & 자른 값 따로 저장
      for(var j = 0; j < i; j++){               //남아있는 값 돌아가면서
          sum = firstnum + numbers[j];          //더하고
          if(!answer.includes(sum)){            //중복제거
              answer.push(sum);
          }
      }
  }
  answer.sort(function(a, b){                   //정렬
      return a-b; 
  });
  return answer;
}

/*

arr.shift()
- 배열 첫자리 삭제, 원본에 덮어씀
- 리턴값 : 삭제된 값

arr.includes(elements)
- arr안에 elements가 있는지 판단
- ture or false

*/