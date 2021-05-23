function solution(n)
{
    let ans = 0;
    while(n>0){
        if(n%2===0){
            //순간이동이 가능하다.
            n/=2;
        }else{
            //홀수라서 순간이동이 안된다면
            n-=1;
            ans+=1;
        }
    }
    return ans;
}

console.log(solution(5));
console.log(solution(6));
console.log(solution(5000));