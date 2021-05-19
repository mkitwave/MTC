function solution(answers) {
    var answer = [];
    var one = [1, 2, 3, 4, 5];
    var two = [2, 1, 2, 3, 2, 4, 2, 5];
    var three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
    var ans = [0, 0, 0];
    var temp = 0, max = 0;
    for(var i = 0 ; i<answers.length ; i++){
        if(answers[i] === one[temp]){
            ans[0]++;
        }
        temp++;
        if(temp === 5){
            temp = 0;
        }
    }
    temp = 0;
    for(var i = 0 ; i<answers.length ; i++){
        if(answers[i] === two[temp]){
            ans[1]++;
        }
        temp++;
        if(temp === 8){
            temp = 0;
        }
    }
    temp = 0;
    for(var i = 0 ; i<answers.length ; i++){
        if(answers[i] === three[temp]){
            ans[2]++;
        }
        temp++;
        if(temp === 10){
            temp = 0;
        }
    }
    for(var i = 0 ; i<3 ; i++){
        if(ans[i]>max) max = ans[i];
    }
    for(var i = 0 ; i<3 ; i++){
        if(ans[i]===max) answer.push(i+1);
    }
    return answer;
  }