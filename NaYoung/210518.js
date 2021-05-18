function solution(arr) { 
    var answer = []; 
    var prev; 
    for(var i = 0 ,iLen = arr.length; i < iLen; i++) { 
        if(prev === arr[i]) continue 
        else { 
            prev = arr[i]; answer.push(prev); 
        } 
    } 
    return answer; }

