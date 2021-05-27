function solution(a,b){
    const days=["SUN","MON","TUE","WED","THU","FRI","SAT"];
    let today=new Date(2016,a-1,b).getDay();
    return days[today];
}

console.log(solution(5,24));