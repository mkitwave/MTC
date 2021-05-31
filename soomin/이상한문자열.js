//무려 12점이나 받은 문제!!
function solution(s) {
    let answer = s.split(' ');
    let newArr=[];
    for(let i=0;i<answer.length;i++){
        for(let j=0;j<answer[i].length;j++){
            if(j%2===0){
               newArr.push(answer[i][j].toUpperCase()); 
            }else{
                newArr.push(answer[i][j].toLowerCase());
            }
        }newArr.push(' ')
    }
    newArr.pop()
    return newArr.join('');
}

console.log(solution("try hello world"));
