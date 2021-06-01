function solution(participant, completion) {
    let answer = '';
    console.log(participant.sort());
    console.log(completion.sort());
    for(let i=0;i<participant.length;i++){
        //p[0]=ana c[0]=ana
        //p[1]=mislav c[1]=mislav
        //p[2]=mislav c[2]= stanko =>어? 다르다 answer=mislav
        //p[3]=stanko p[3]=undefined => 여기서 멈추지않으면 답이 stanko가 나올 것임
        if(participant[i]!==completion[i]){
            answer=participant[i];
            return answer;
        }
    }
}

console.log(solution(["leo","kiki","eden"],["eden","kiki"]));