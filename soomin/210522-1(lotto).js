function solution(lottos,win_nums){
    let count=0;
    let zero_count=lottos.filter((e)=>e===0).length;
    for(let i=0;i<win_nums.length;i++){
        if(win_nums.includes(lottos[i])===true) count+=1;
    }
    let min_count=ranking(count);
    let max_count=ranking(count+zero_count);
    
    return [max_count,min_count];
}

function ranking(count){
    let rank=0;
    switch(count){
        case 6:rank=1;break;
        case 5:rank=2;break;
        case 4:rank=3;break;
        case 3:rank=4;break;
        case 2:rank=5;break;
        default:rank=6;break;
    }
    return rank;
}

console.log(solution([44,1,0,0,31,25],[31,10,45,1,6,19]));
console.log(solution([0,0,0,0,0,0],[38,19,20,40,15,25]));
console.log(solution([45,4,35,20,3,9],[20,9,3,45,4,35]));