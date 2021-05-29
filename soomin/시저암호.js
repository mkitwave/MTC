function solution(s, n) {
    let upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    let lower = "abcdefghijklmnopqrstuvwxyz";
    let answer= '';
    for(let i=0;i<s.length;i++){
        let text=s[i];
        if(text===' '){
            answer+=' ';
            continue;
        }
        
        let textArr=upper.includes(text)?upper:lower;
        let idx=textArr.indexOf(text)+n;
        if(idx>=textArr.length) idx-=textArr.length;
        answer+=textArr[idx];
    }
    return answer;

}

console.log(solution("AB",1));
console.log(solution("z",1));
console.log(solution("a B z",4));