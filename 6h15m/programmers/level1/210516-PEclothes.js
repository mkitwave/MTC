// 실패(아직 이유 못 찾음)

function solution(n, lost, reserve) {
    var temp = 0;
    lost.sort(function(a, b){return a-b;});
    reserve.sort(function(a, b){return a-b;});
    for(var i = 0; i < lost.length; i++){
        if(reserve.includes(lost[i])){
            reserve.splice(reserve.indexOf(lost[i]), 1);
            temp += 1;
        } else if(reserve.includes(lost[i] - 1)){
            if(lost.includes(lost[i] - 1)){
                continue;
            }
            reserve.splice(reserve.indexOf(lost[i] - 1), 1);
            temp += 1;
        } else if(reserve.includes(lost[i] + 1)){
            if(lost.includes(lost[i] + 1)){
                continue;
            }
            reserve.splice(reserve.indexOf(lost[i] + 1), 1);
            temp += 1;
        }
    return n - (lost.length - temp);
    }
}